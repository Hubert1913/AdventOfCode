def main():
    inp = open("data.in").read().split("\n\n")
    maze_inp = list(map(lambda x: list(x), inp[0].split("\n")))
    maze = []
    robot = [0, 0]
    for i in range(len(maze_inp)):
        maze.append([])
        for j in range(len(maze_inp[0])):
            if maze_inp[i][j] == "#":
                maze[i].append(1)
                maze[i].append(1)
            elif maze_inp[i][j] == "O":
                maze[i].append("[")
                maze[i].append("]")
            else:
                if maze_inp[i][j] == "@":
                    robot = [i, 2*j]
                maze[i].append(0)
                maze[i].append(0)
    moves = "".join(list(map(lambda x: x.strip(), inp[1].split("\n"))))

    dirs = {
        "^": [-1, 0],
        ">": [0, 1],
        "v": [1, 0],
        "<": [0, -1]
    }

    for move in moves:
        d = dirs[move]
        next_robot = [robot[0] + d[0], robot[1] + d[1]]
        if maze[next_robot[0]][next_robot[1]] == 1:
            continue
        elif maze[next_robot[0]][next_robot[1]] == 0:
            robot = next_robot
            continue
        else:
            if move == ">" or move == "<":
                walk = next_robot
                while maze[walk[0]][walk[1]] == "[" or maze[walk[0]][walk[1]] == "]":
                    walk = [walk[0] + d[0], walk[1] + d[1]]
                if maze[walk[0]][walk[1]] == 1:
                    continue
                else:
                    d_op = [-d[0], -d[1]]
                    while walk != next_robot:
                        next_walk = [walk[0] + d_op[0], walk[1] + d_op[1]]
                        maze[walk[0]][walk[1]] = maze[next_walk[0]][next_walk[1]]
                        walk = next_walk
                    maze[next_robot[0]][next_robot[1]] = 0
                    robot = next_robot
            else:
                lines = []
                if maze[next_robot[0]][next_robot[1]] == "[":
                    lines.append({(next_robot[0], next_robot[1]), (next_robot[0], next_robot[1] + 1)})
                else:
                    lines.append({(next_robot[0], next_robot[1] - 1), (next_robot[0], next_robot[1])})

                free = False
                obstacle = False
                while not free:
                    free = True
                    next_line = set()
                    for pos in lines[len(lines)-1]:
                        next_pos = (pos[0] + d[0], pos[1] + d[1])
                        if maze[next_pos[0]][next_pos[1]] == 1:
                            obstacle = True
                            break
                        elif maze[next_pos[0]][next_pos[1]] == "[":
                            next_line.add(next_pos)
                            next_line.add((next_pos[0], next_pos[1] + 1))
                            free = False
                        elif maze[next_pos[0]][next_pos[1]] == "]":
                            next_line.add(next_pos)
                            next_line.add((next_pos[0], next_pos[1] - 1))
                            free = False

                    if obstacle:
                        break
                    lines.append(next_line)
                if (not obstacle) and free:
                    for line in reversed(lines):
                        for pos in line:
                            next_pos = (pos[0] + d[0], pos[1] + d[1])
                            maze[next_pos[0]][next_pos[1]] = maze[pos[0]][pos[1]]
                            maze[pos[0]][pos[1]] = 0

                    robot = next_robot

    total = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "[":
                total += 100 * i + j

    print(total)


if __name__ == '__main__':
    main()