import os
from collections import Counter

def process_input(lines):
    # Use list comprehension for initial parsing - more efficient than loop
    number_pairs = [tuple(map(int, line.strip().split())) for line in lines]
    
    # Use zip for more efficient column extraction
    first_column, second_column = zip(*number_pairs)
    
    # Convert to lists since we need mutability for sorting
    first_column = list(first_column)
    second_column = list(second_column)
    
    first_column.sort()
    second_column.sort()

    # Use sum with generator expression instead of creating intermediate list
    differences = sum(abs(a - b) for a, b in zip(first_column, second_column))

    # Use Counter for more efficient counting
    from collections import Counter
    first_counts = Counter(first_column)
    second_counts = Counter(second_column)

    # Calculate similarity more efficiently
    similarity = sum(num * count * second_counts[num] 
                    for num, count in first_counts.items())

    return differences, similarity

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