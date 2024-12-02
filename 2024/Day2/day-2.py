input_file_name = 'day-2-input.txt'

data = open(input_file_name, 'r').read().split('\n')


def is_report_safe(report) -> bool:
    is_ascending = None

    for i in range(len(report)):
        if i == 0:
            continue

        diff_step = abs(report[i]-report[i-1])
        if diff_step < 1 or diff_step > 3:
            return False

        if i == 1:
            if report[i] > report[i-1]:
                is_ascending = True
            else:
                is_ascending = False
            continue

        if report[i] < report[i-1]:
            if is_ascending:
                return False

        if report[i] > report[i-1]:
            if is_ascending == False:
                return False

    return True

safe_report_count = 0

for d in data:
    report = list(map(int, d.split()))
    if is_report_safe(report):
        safe_report_count += 1

print("safe report count: ", safe_report_count)
