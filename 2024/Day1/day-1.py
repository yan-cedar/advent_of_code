input_file_name = 'day-1-input.txt'

data = open(input_file_name, 'r').read().split('\n')

left_nums = []
right_nums = []

for d in data:
    left, right = d.split()
    left_nums.append(int(left))
    right_nums.append(int(right))

left_nums = sorted(left_nums)
right_nums = sorted(right_nums)

total_distance = 0

for i in range(len(left_nums)):
    total_distance += abs(left_nums[i] - right_nums[i])

print("total distance: ", total_distance)
