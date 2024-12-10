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

for update in updates:
    update_list = update.split(',')
    order_facts = build_update_fact(update_list)
    if check_rule(order_facts, rule_orders):
        print(f'update {update_list} follows the rule!')
        result += int(update_list[len(update_list)//2])

print('Part 1 Result:', result)
