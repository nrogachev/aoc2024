from pathlib import Path

def process_input(lines):
    grid = [list(line.strip()) for line in lines]
    rows, cols = len(grid), len(grid[0])
    part1 = part2 = 0

    # Directions for part1 (y, x)
    directions = [
        [(-1, 0), (-2, 0), (-3, 0)],  # up
        [(1, 0), (2, 0), (3, 0)],     # down
        [(0, -1), (0, -2), (0, -3)],  # left
        [(0, 1), (0, 2), (0, 3)],     # right
        [(-1, -1), (-2, -2), (-3, -3)],  # diagonal up-left
        [(-1, 1), (-2, 2), (-3, 3)],     # diagonal up-right
        [(1, -1), (2, -2), (3, -3)],     # diagonal down-left
        [(1, 1), (2, 2), (3, 3)]         # diagonal down-right
    ]

    for i in range(rows):
        for j in range(cols):
            # Part 1
            if grid[i][j] == 'X':
                for direction in directions:
                    valid = True
                    word = 'X'
                    for dy, dx in direction:
                        new_i, new_j = i + dy, j + dx
                        if not (0 <= new_i < rows and 0 <= new_j < cols):
                            valid = False
                            break
                        word += grid[new_i][new_j]
                    if valid and word == 'XMAS':
                        part1 += 1

            # Part 2
            if (0 < i < rows-1 and 0 < j < cols-1 and 
                grid[i][j] == 'A'):
                diag1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
                diag2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
                if (diag1 in ('MAS', 'SAM') and 
                    diag2 in ('MAS', 'SAM')):
                    part2 += 1

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