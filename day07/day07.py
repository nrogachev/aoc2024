from pathlib import Path
from time import perf_counter as timer
import math

def check(collected, numbers, target):
    n1 = collected + numbers[0]
    n2 = collected * numbers[0]
    if len(numbers) == 1:
        if n1 == target or n2 == target:
            return True
        else:
            return False
    if n1 > target and n2 > target:
        return False
    elif n1 < target and n2 > target:
        return check(n1, numbers[1:], target)
    elif n1 > target and n2 < target:
        return check(n2, numbers[1:], target)
    else:
        return check(n1, numbers[1:], target) or check(n2, numbers[1:], target)

def process_input(lines):
    # print(lines)
    equations = []
    for line in lines:
        parts = line.split(':') 
        equations.append((int(parts[0]), list(map(int, parts[1].strip().split()))))
    # print(equations)

    start_time = timer()    
    part1 = 0
    for equation in equations:
        # print(equation)
        numbers = equation[1]
        if check(numbers[0], numbers[1:], equation[0]):
            part1 += equation[0]

    end_time = timer()  
    print(f"Execution time Part 1: {end_time - start_time:.3f} seconds")

    start_time = timer()    
    part2 = 0
    end_time = timer()  
    print(f"Execution time Part 2: {end_time - start_time:.3f} seconds")

    return part1, part2

def main():
    start_time = timer()    
    file_path = Path(__file__).parent / 'input.txt'
    
    with open(file_path) as file:
        lines = file.readlines()
    result = process_input(lines)
    end_time = timer()
    print(f"Execution time Total: {end_time - start_time:.3f} seconds")
    print(f"Result: {result}")
    return result

if __name__ == "__main__":
    main()