from pathlib import Path

def swap(update, rule):
    update[rule[1]], update[rule[0]] = update[rule[0]], update[rule[1]]
    return update

def is_ordered(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update and update[rule[0]] > update[rule[1]]:
            return False
    return True

def check_and_swap(update, rules):
    swapped = False
    for rule in rules:
        if rule[0] in update and rule[1] in update and update[rule[0]] > update[rule[1]]:
            swap(update, rule)
            swapped = True
    return update, swapped

def process_input(lines):
    # print(lines)
    rules = []
    updates = []
    split = False
    for line in lines:
        if line == '\n':
            split = True
            continue
        if split:
            index_map = {num: idx for idx, num in enumerate(list(map(int, line.strip().split(','))))}
            updates.append(index_map)
        else:
            n1, n2 = map(int, line.strip().split('|'))
            rules.append((n1, n2))
    # print(rules)    
    # print(updates)

    ordered_updates = []
    unordered_updates = []
    for update in updates:
        if is_ordered(update, rules):
            ordered_updates.append(update)
        else:
            unordered_updates.append(update)

    part1 = 0
    for update in ordered_updates:
        for k,v in update.items():
            if v == len(update) // 2:
                part1 += k

    part2 = 0
    for update in unordered_updates:
        swapped = True
        while swapped:
            update, swapped = check_and_swap(update, rules)
        for k,v in update.items():
            if v == len(update) // 2:
                part2 += k

    return part1, part2

def main():
    file_path = Path(__file__).parent / 'input.txt'
    
    with open(file_path) as file:
        lines = file.readlines()
    result = process_input(lines)
    print(result)
    return result

if __name__ == "__main__":
    main()