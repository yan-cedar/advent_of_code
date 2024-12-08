input_file_name = 'day-7-input.txt'

lines = open(input_file_name, 'r').read().split('\n')

def calibrate(nums, expected) -> int:
    if len(nums) < 2:
        return 0

    if len(nums) == 2:
        if nums[0] + nums[1] == expected or nums[0] * nums[1] == expected:
            return expected
        else:
            return 0

    if nums[-1] + calibrate(nums[:-1], expected - nums[-1]) == expected or \
            nums[-1] * calibrate(nums[:-1], expected/nums[-1]) == expected:
       return expected
    else:
       return 0


def calibrate_line(input_line) -> int:
    expected, nums = input_line.split(': ')
    nums_list = [int(n) for n in nums.split(' ')]

    return calibrate(nums_list, int(expected))


def triple_calibrate_line(input_line) -> int:
    expected, nums = input_line.split(': ')
    nums_list = [int(n) for n in nums.split(' ')]

    return triple_calibrate(nums_list, int(expected))

result = 0
for line in lines:
    result += calibrate_line(line)

print('Result of Part 1:', result)

### part 2
def concat(num_1: int, num_2: int):
    len_num2 = len(str(num_2))

    return num_1 * (10 ** len_num2) + num_2

def de_concat(num: int, tail_int: int):
    len_tail_int = len(str(tail_int))

    return num // (10 ** len_tail_int)

def triple_calibrate(nums, expected):
    if len(nums) < 2:
        return 0

    if len(nums) == 2:
        if nums[0] + nums[1] == expected or nums[0] * nums[1] == expected \
            or concat(nums[0], nums[1]) == expected:
            return expected
        else:
            return 0

    if nums[-1] + triple_calibrate(nums[:-1], expected - nums[-1]) == expected or \
            nums[-1] * triple_calibrate(nums[:-1], expected//nums[-1]) == expected or \
            concat(triple_calibrate(nums[:-1], de_concat(expected, nums[-1])), nums[-1]) == expected:
        return expected
    else:
       return 0

result = 0
for line in lines:
    result += triple_calibrate_line(line)

print('Result of part 2:', result)

