input_file_name = 'day-4-test-input.txt'

lines = open(input_file_name, 'r').read().split('\n')

total_samples = []

### horizontal lines
# for l in lines:
#     total_samples.append(l)
#     total_samples.append(l[::-1])

### vertical lines
for i in range(len(lines[0])):
    line = ''
    for l in lines:
        line += l[i]
    total_samples.append(line)
    total_samples.append(line[::-1])

### diagonal lines
for i in range(len(lines)):
    line = ''


    for j in range(len(lines[i])):
        line += lines[j][i]

    print("diag line: ", line)
    total_samples.append(line)
    total_samples.append(line[::-1])

print(total_samples)

xmas = 'XMAS'
xmas_reverse = xmas[::-1]

def line_scan(line, target):
    count  = 0

    i = line.find(target, 0)
    while i >= 0:
        count += 1
        i = line.find(target, i+len(target))

    return count

line_test = 'XMASXMASXMASXMASXMAS'


ctr = 0
for l in total_samples:
    ctr += line_scan(l, xmas)
    ctr += line_scan(l, xmas_reverse)

print("ctr: ", ctr)


