from pathlib import Path
from time import perf_counter as timer

def check(collected, numbers, target, with_concat=False):
    n1 = collected + numbers[0]
    n2 = collected * numbers[0]
    if with_concat:
        n3 = int(str(collected) + str(numbers[0]))

    if len(numbers) == 1:
        return n1 == target or n2 == target or (with_concat and n3 == target)

    result = False
    if with_concat and n3 <= target and not result:
        result = result or check(n3, numbers[1:], target, with_concat)
    if n2 <= target and not result:
        result = result or check(n2, numbers[1:], target, with_concat)
    if n1 <= target and not result:
        result = result or check(n1, numbers[1:], target, with_concat)
    return result
    
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
    for equation in equations:
        # print(equation)
        numbers = equation[1]
        if check(numbers[0], numbers[1:], equation[0], True):
            # print(equation)
            part2 += equation[0]    
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