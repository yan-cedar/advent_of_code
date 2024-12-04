from urllib.parse import quote_plus

input_file_name = 'day-3-input.txt'

chars = open(input_file_name, 'r').read().split('\n')
text = "".join(chars)

result = 0

key_start = 'mul('
key_end = ')'


def has_space(string):
    if " " in string:
        return True

    return False


i = 0

while i < len(text):
    start = text.find(key_start, i)
    if start == -1:
        break

    end = text.find(key_end, start)
    if end == -1:
        break

    target = text[start+len(key_start):end]

    try:
        left, right = target.split(',')
        result += int(left) * int(right)
    except ValueError:
        found = target.rfind(key_start)

        if found != -1:
            inner_found = target[found+len(key_start):end]
            try:
                left, right = inner_found.split(',')
                if has_space(left) or has_space(right):
                    i = end + 1
                    continue

                result += int(left) * int(right)
            except ValueError:
                i = end + 1
                continue

    i = end + 1

print('result: ', result)
