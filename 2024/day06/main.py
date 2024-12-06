import copy


def main():
    inp = open("data.in").readlines()

    maze = []
    guard = []
    for i, line in enumerate(inp):
        if line.strip() != "":
            l = list(line)
            if "^" in l:
                guard = [l.index("^"), i]
                l[guard[0]] = "."
            maze.append(l)

    dirs = [0,-1,0,1,0]
    index = 0
    visited = set()
    out = False
    n = len(maze)
    m = len(maze[0])

    while not out:
        visited.add((guard[0], guard[1]))
        next_pos = [guard[0] + dirs[index], guard[1] + dirs[index+1]]
        if next_pos[1] >= n or next_pos[0] >= m or next_pos[0] < 0 or next_pos[1] < 0:
            out = True
        elif maze[next_pos[1]][next_pos[0]] == "#":
            index -= 1
            if index < 0:
                index += 4
        else:
            guard = next_pos

    print(len(visited))


def simulate(maze, guard):
    dirs = [0, -1, 0, 1, 0]
    index = 0
    visited = set()
    out = False
    n = len(maze)
    m = len(maze[0])
    tp = set()

    while not out:
        if (guard[0], guard[1], index) in tp:
            return True
        visited.add((guard[0], guard[1]))
        next_pos = [guard[0] + dirs[index], guard[1] + dirs[index + 1]]
        if next_pos[1] >= n or next_pos[0] >= m or next_pos[0] < 0 or next_pos[1] < 0:
            out = True
        elif maze[next_pos[1]][next_pos[0]] == "#":
            tp.add((guard[0], guard[1], index))
            index -= 1
            if index < 0:
                index += 4
        else:
            guard = next_pos

    return False


def main_part_2():
    inp = open("data.in").readlines()

    maze = []
    guard = []
    for i, line in enumerate(inp):
        if line.strip() != "":
            l = list(line.strip())
            if "^" in l:
                guard = [l.index("^"), i]
                l[guard[0]] = "."
            maze.append(l)

    # this is super slow, but passes so whatever
    total = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "#" or [j, i] == guard:
                continue
            maze_cop = copy.deepcopy(maze)
            maze_cop[i][j] = "#"
            if simulate(maze_cop, guard):
                total += 1

    print(total)


if __name__ == '__main__':
    # main()
    main_part_2()
    