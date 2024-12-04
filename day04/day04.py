from pathlib import Path

def process_input(lines):
    # print(lines)
    part1 = 0
    part2 = 0

    grid = [list(line.strip()) for line in lines]
    # print(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # print(i, j)
            # part 1
            if grid[i][j] == 'X':
                # check upwards
                if i >= 3 and grid[i-1][j] == 'M' and grid[i-2][j] == 'A' and grid[i-3][j] == 'S':  
                    part1 += 1
                # check downwards
                if i <= len(grid) - 4 and grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
                    part1 += 1
                # check left    
                if j >= 3 and grid[i][j-1] == 'M' and grid[i][j-2] == 'A' and grid[i][j-3] == 'S':
                    part1 += 1
                # check right
                if j <= len(grid[i]) - 4 and grid[i][j+1] == 'M' and grid[i][j+2] == 'A' and grid[i][j+3] == 'S':
                    part1 += 1
                # check diagonal upwards left
                if i >= 3 and j >= 3 and grid[i-1][j-1] == 'M' and grid[i-2][j-2] == 'A' and grid[i-3][j-3] == 'S':
                    part1 += 1  
                # check diagonal upwards right
                if i >= 3 and j <= len(grid[i]) - 4 and grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S':
                    part1 += 1      
                # check diagonal downwards left
                if i <= len(grid) - 4 and j >= 3 and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
                    part1 += 1
                # check diagonal downwards right
                if i <= len(grid) - 4 and j <= len(grid[i]) - 4 and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
                    part1 += 1
            # part 2
            if i >=1 and i <= len(grid)-2 and j >=1 and j <= len(grid[i])-2 and grid[i][j] == 'A':
                diagonal_1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
                diagonal_2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]
                if diagonal_1 == 'MAS' or diagonal_1 == 'SAM':
                    if diagonal_2 == 'MAS' or diagonal_2 == 'SAM':
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