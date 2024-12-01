def process_input(lines):
    # Convert each line into pairs of numbers
    number_pairs = []
    for line in lines:
        # Split the line and convert to integers
        first, second = map(int, line.strip().split())
        number_pairs.append((first, second))
    
    # At this point number_pairs is a list of tuples like [(n1, n2), (n1, n2), ...]
    # You can access columns like this:
    first_column = [pair[0] for pair in number_pairs]
    second_column = [pair[1] for pair in number_pairs]
    
    first_column.sort()
    second_column.sort()

    #print(first_column)
    #print(second_column)

    differences = []
    for i in range(len(first_column)):
        diff = abs(first_column[i] - second_column[i])
        differences.append(diff)

    occurrences = {num: (first_column.count(num), second_column.count(num)) for num in first_column}
    # print(occurrences)

    similarity = 0
    for key, value in occurrences.items():
        similarity += key * value[0] * value[1]

    return sum(differences), similarity

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    result = process_input(lines)
    print(result)
    return result  # Return value for testing

if __name__ == "__main__":
    main()