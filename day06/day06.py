from pathlib import Path

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

    pos = start
    dir = map[start[0]][start[1]]
    map[start[0]][start[1]] = 'X'
    visited = set([start])
    visited_with_dir = set([(start, dir)])
    obstacles = set()
    while True:
        next_move = (pos[0] + directions[dir][0], pos[1] + directions[dir][1])
        if not (0 <= next_move[0] < rows and 0 <= next_move[1] < cols):
            break

        if (next_move, dir) in visited_with_dir:
            break
        o_dir = rotation_order[(rotation_order.index(dir) + 1) % 4]
        if map[next_move[0]][next_move[1]] == '#':
            # hit a wall, turn right
            dir = o_dir
            continue
        else:   
            # obstacle check
            o_next_move = (pos[0] + directions[o_dir][0], pos[1] + directions[o_dir][1])
            while map[o_next_move[0]][o_next_move[1]] != '#':
                if (o_next_move, o_dir) in visited_with_dir:
                    obstacles.add(next_move)
                    break
                o_next_move = (o_next_move[0] + directions[o_dir][0], o_next_move[1] + directions[o_dir][1])
                if not (0 <= o_next_move[0] < rows and 0 <= o_next_move[1] < cols):
                    break
            pos = next_move
            # map[pos[0]][pos[1]] = 'X'
            visited.add(pos)
            visited_with_dir.add((pos, dir))
    # for row in range(rows):
    #     print(''.join(map[row]))
    part1 = len(visited)

    # print(obstacles)
    part2 = len(obstacles)
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