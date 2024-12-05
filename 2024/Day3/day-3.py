input_file_name = 'day-3-input.txt'

chars = open(input_file_name, 'r').read().split('\n')
text = "".join(chars)

key_start = 'mul('
key_end = ')'
enable_key = 'do()'
disable_key = "don't()"

### part 1
def get_mul_range(text, start_idx, end_idx):
    result = 0

    i = start_idx

    while i <= end_idx:
        start = text.find(key_start, i, end_idx)
        if start == -1:
            break

        end = text.find(key_end, start)
        if end == -1:
            break

        target = text[start + len(key_start):end]

        try:
            left, right = target.split(',')
            result += int(left) * int(right)
        except ValueError:
            found = target.rfind(key_start)

            if found != -1:
                inner_found = target[found + len(key_start):end]
                try:
                    left, right = inner_found.split(',')
                    if " " in left or " " in right:
                        i = end + 1
                        continue

                    result += int(left) * int(right)
                except ValueError:
                    i = end + 1
                    continue

        i = end + 1

    return result

result = get_mul_range(text, 0, len(text)-1)
print("part 1 result: ", result)

### part 2
i = 0
res = 0

while i < len(text):
    disable_start = text.find(disable_key, i)
    if disable_start == -1:
        # no more disable key
        res += get_mul_range(text, i, len(text)-1)
        break

    # found disable key
    res += get_mul_range(text, i, disable_start-1)

    i = disable_start + len(disable_key)
    enable_start = text.find(enable_key, i)

    if enable_start == -1:
        # disabled till end
        break
    else:
        i = enable_start + len(enable_key)

print("part 2 result: ", res)
