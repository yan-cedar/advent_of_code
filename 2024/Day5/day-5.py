from collections import defaultdict
input_file_name = 'day-5-input.txt'

lines = open(input_file_name, 'r').read().split('\n')
rules = []
idx = 0

for line in lines:
    if line == '':
        break

    rules.append(line)
    idx+=1

updates = lines[idx+1:]


def build_update_fact(update_list):
    order_facts = defaultdict(lambda: {'before': set(), 'after': set()})

    for i, item in enumerate(update_list):
        for j in range(i):
            order_facts[item]['before'].add(update_list[j])
        for j in range(i+1, len(update_list)):
            order_facts[item]['after'].add(update_list[j])

    return order_facts


def build_rule(rules):
    rule_orders = defaultdict(lambda: {'before': set(), 'after': set()})

    for r in rules:
        r_list = r.split('|')
        rule_orders[r_list[0]]['after'].add(r_list[1])
        rule_orders[r_list[1]]['before'].add(r_list[0])

    return rule_orders


def check_rule(order_facts, rule_orders):
    for key in order_facts.keys():
        for before in order_facts[key]['before']:
            if before in rule_orders[key]['after']:
                return False

        for after in order_facts[key]['after']:
            if after in rule_orders[key]['before']:
                return False

    return True

rule_orders = build_rule(rules)

result = 0
incorrect_updates = []

for update in updates:
    update_list = update.split(',')
    order_facts = build_update_fact(update_list)
    if check_rule(order_facts, rule_orders):
        result += int(update_list[len(update_list)//2])
    else:
        incorrect_updates.append(update_list)

print('Part 1 Result:', result)

### part 2
def fix_incorrect_update(incorrect_update, rule_orders):
    correct_update = []

    for update in incorrect_update:
        if len(correct_update) == 0:
            correct_update.append(update)
            continue

        for i in range(len(correct_update)):
            if update in rule_orders[correct_update[i]]['before']:
                correct_update.insert(i, update)
                break

        if update in correct_update:
            continue

        for i in range(len(correct_update)-1, -1, -1):
            if update in rule_orders[correct_update[i]]['after']:
                correct_update.insert(i+1, update)
                break

    return correct_update


result = 0
for incorrect_update in incorrect_updates:
    correct_update = fix_incorrect_update(incorrect_update, rule_orders)
    result += int(correct_update[len(correct_update) // 2])

print('Result of Part 2:', result)
