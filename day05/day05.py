from pathlib import Path

def swap(update, rule):
    update[0][rule[1]], update[0][rule[0]] = update[0][rule[0]], update[0][rule[1]]
    update[1][update[0][rule[1]]], update[1][update[0][rule[0]]] = update[1][update[0][rule[0]]], update[1][update[0][rule[1]]]
    return update

def check_rule(update, rule):
    return rule[0] in update[0] and rule[1] in update[0] and update[0][rule[0]] > update[0][rule[1]]

def is_ordered(update, rules):
    for rule in rules:
        if check_rule(update, rule):
            return False
    return True

def check_and_swap(update, rules):
    swapped = False
    for rule in rules:
        if check_rule(update, rule):
            swap(update, rule)
            swapped = True
    return update, swapped

def process_input(lines):
    # print(lines)
    rules = []
    updates = []

    split_idx = lines.index('\n')

    rules = [tuple(map(int, line.strip().split('|'))) 
             for line in lines[:split_idx]]
    
    for line in lines[split_idx + 1:]:
        if not line.strip():
            continue
        numbers = list(map(int, line.strip().split(',')))
        index_map = {num: idx for idx, num in enumerate(numbers)}
        reverse_map = {idx: num for num, idx in index_map.items()}
        updates.append((index_map, reverse_map))

    # print(rules)    
    # print(updates)

    ordered = []
    unordered = []
    for update in updates:
        (ordered if is_ordered(update, rules) else unordered).append(update)

    part1 = sum(update[1][len(update[1]) // 2] for update in ordered)

    part2 = 0
    for update in unordered:
        swapped = True
        while swapped:
            update, swapped = check_and_swap(update, rules)
        part2 += update[1][len(update[1]) // 2]

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