from pathlib import Path

def process_input(lines):
    print(lines)
    part1 = 0
    part2 = 0
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