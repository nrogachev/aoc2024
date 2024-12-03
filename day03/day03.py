import re
from pathlib import Path

def process_input(lines):
    pattern = r'(do\(\)|don\'t\(\))|(mul\((\d{1,3}),(\d{1,3})\))'
    text = ''.join(lines)
    matches = list(re.finditer(pattern, text))
    
    part1, part2 = 0, 0
    last_control = None
    
    for match in matches:
        if match.group(1):  # Control group (do/don't)
            last_control = match.group(1)
        else:  # mul group
            num1, num2 = map(int, (match.group(3), match.group(4)))
            product = num1 * num2
            part1 += product  
            if last_control is None or last_control == "do()":
                part2 += product 

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