import os

def process_input(lines):
    print(lines)
    part1 = 0
    part2 = 0
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