from pathlib import Path
from timeit import default_timer as timer

def walk_map(map, start, directions, rotation_order):
    rows, cols = len(map), len(map[0])
    pos = start
    dir = map[start[0]][start[1]]
    visited = set([start])
    visited_with_dir = set([(start, dir)])
    loop_found = False
    while True:
        next_move = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
        if not (0 <= next_move[0] < rows and 0 <= next_move[1] < cols):
            # out of bounds
            break
        if map[next_move[0]][next_move[1]] == '#':
            # hit a wall, turn right
            dir = rotation_order[(rotation_order.index(dir) + 1) % 4]
            continue
        else:   
            if (next_move, dir) in visited_with_dir:
                loop_found = True
                break
            pos = next_move
            visited.add(pos)
            visited_with_dir.add((pos, dir))
    return visited, loop_found

def process_input(lines):
    # print(lines)s
    map = [list(line.strip()) for line in lines]
    rows, cols = len(map), len(map[0])

    start = next(
        ((row, col)
        for row in range(rows)
        for col in range(cols)
        if map[row][col] in '<^>v')
    , None)
    # print(start)

    directions = {
        '^': (-1, 0),  # up
        '>': (0, 1),   # right
        'v': (1, 0),   # down
        '<': (0, -1)  # left
    }
    rotation_order = ['^', '>', 'v', '<']
    # print(directions[map[start[0]][start[1]]])
    start_time = timer()
    visited, loop_found = walk_map(map, start, directions, rotation_order)
    end_time = timer()
    print(f"Execution time Part 1: {end_time - start_time:.3f} seconds")
    # for row in range(rows):
    #     print(''.join(map[row]))
    part1 = len(visited)
    # print(loop_found)

    start_time = timer()
    pos = start
    dir = map[start[0]][start[1]]
    obstacles = set()
    while True:
        next_move = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
        # print(next_move)
        if not (0 <= next_move[0] < rows and 0 <= next_move[1] < cols):
            break
        if map[next_move[0]][next_move[1]] == '#':
            # hit a wall, turn right
            dir = rotation_order[(rotation_order.index(dir) + 1) % 4]
            continue
        else:   
            # obstacle check - add new wall on the way and see if walking changed map creates a loop
            if next_move not in obstacles and next_move != start:
                new_map = [row[:] for row in map]
                new_map[next_move[0]][next_move[1]] = '#'
                _, loop_found = walk_map(new_map, start, directions, rotation_order)
                if loop_found:
                    obstacles.add(next_move)
            pos = next_move       

    # print(obstacles)
    end_time = timer()
    print(f"Execution time Part 2: {end_time - start_time:.3f} seconds")
    part2 = len(obstacles)
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