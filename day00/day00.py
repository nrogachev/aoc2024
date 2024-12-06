from pathlib import Path
from time import perf_counter as timer
def process_input(lines):
    print(lines)
    part1 = 0
    part2 = 0
    return part1, part2

def main():
    start_time = timer()    
    file_path = Path(__file__).parent / 'input.txt'
    
    with open(file_path) as file:
        lines = file.readlines()
    result = process_input(lines)
    end_time = timer()
    print(f"Execution time Total: {end_time - start_time:.3f} seconds")
    print(result)
    return result

if __name__ == "__main__":
    main()