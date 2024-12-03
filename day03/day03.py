import os
import re

def process_input(lines):
    # Matches mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    control_pattern = r'do\(\)|don\'t\(\)'
    matches = []

    for line in lines:
        matches.extend(re.findall(pattern, line))

    # print(matches)

    part1 = 0
    for match in matches: 
        part1 += int(match[0]) * int(match[1])
    
    part2 = 0
    text = ''.join(lines)
    
    mul_matches = list(re.finditer(pattern, text))
    control_matches = list(re.finditer(control_pattern, text))
    for mul_match in mul_matches:
        # Find the last control match before this mul
        last_control = None
        current_control_idx = 0
        while (current_control_idx < len(control_matches) and 
               control_matches[current_control_idx].start() < mul_match.start()):
            last_control = control_matches[current_control_idx]
            current_control_idx += 1
        
        # If we found a control and it's "do()", multiply the numbers
        if last_control is None or last_control.group() == "do()":
            num1, num2 = map(int, mul_match.groups())
            part2 += num1 * num2

    return part1, part2

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'input.txt')
        
    with open(file_path, 'r') as file:
        lines = file.readlines()
    result = process_input(lines)
    print(result)
    return result

if __name__ == "__main__":
    main()