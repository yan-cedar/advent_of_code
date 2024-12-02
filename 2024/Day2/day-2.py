input_file_name = 'day-2-input.txt'

data = open(input_file_name, 'r').read().split('\n')

### Part 1
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

### Part 2
def get_first_fail_point(report):
    is_ascending = None

    for i in range(len(report)):
        if i == 0:
            continue

        diff_step = abs(report[i]-report[i-1])
        if diff_step < 1 or diff_step > 3:
            return i

        if i == 1:
            if report[i] > report[i-1]:
                is_ascending = True
            else:
                is_ascending = False
            continue

        if report[i] < report[i-1]:
            if is_ascending:
                return i

        if report[i] > report[i-1]:
            if is_ascending == False:
                return i

    return None


def is_report_damper_safe(report):
    if is_report_safe(report):
        return True

    fail_point = get_first_fail_point(report)
    while fail_point >= 0:
        damper_report = report[:fail_point] + report[fail_point+1:]
        if is_report_safe(damper_report):
            return True

        fail_point-=1

    return False


damper_safe_report_count = 0

for d in data:
    report = list(map(int, d.split()))
    if is_report_damper_safe(report):
        damper_safe_report_count += 1

print("damper safe report count: ", damper_safe_report_count)
