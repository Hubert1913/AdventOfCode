def part_1():
    inp = open("data.in").readlines()

    maze = []
    s_pos = (-1, -1)

    for i in range(len(inp)):
        line = inp[i]
        if line.strip() != "":
            line_s = list(line.strip())
            maze.append(line_s)
            if "S" in line_s:
                j = line_s.index("S")
                s_pos = (i, j)

    curs = []
    visited = [s_pos]
    steps = 1

    # check north:
    if s_pos[0] - 1 >= 0:
        i, j = s_pos[0] - 1, s_pos[1]
        if maze[i][j] == "|" or maze[i][j] == "7" or maze[i][j] == "F":
            curs.append((i, j))

    # check east:
    if s_pos[1] + 1 < len(maze[0]):
        i, j = s_pos[0], s_pos[1] + 1
        if maze[i][j] == "-" or maze[i][j] == "J" or maze[i][j] == "7":
            curs.append((i, j))

    # check south:
    if s_pos[0] + 1 < len(maze):
        i, j = s_pos[0] + 1, s_pos[1]
        if maze[i][j] == "|" or maze[i][j] == "J" or maze[i][j] == "L":
            curs.append((i, j))

    # check west:
    if s_pos[1] - 1 >= 0:
        i, j = s_pos[0], s_pos[1] - 1
        if maze[i][j] == "-" or maze[i][j] == "L" or maze[i][j] == "F":
            curs.append((i, j))

    while curs[0] != curs[1]:
        next_curs = []
        for cur in curs:
            poss = []
            i, j = cur[0], cur[1]
            if maze[i][j] == "|":
                poss = [(i - 1, j), (i + 1, j)]
            elif maze[i][j] == "-":
                poss = [(i, j - 1), (i, j + 1)]
            elif maze[i][j] == "L":
                poss = [(i - 1, j), (i, j + 1)]
            elif maze[i][j] == "J":
                poss = [(i, j - 1), (i - 1, j)]
            elif maze[i][j] == "7":
                poss = [(i, j - 1), (i + 1, j)]
            elif maze[i][j] == "F":
                poss = [(i, j + 1), (i + 1, j)]

            if poss[0] in visited:
                next_curs.append(poss[1])
            else:
                next_curs.append(poss[0])

            visited.append(cur)

        curs = next_curs
        steps += 1

    print(steps)


def part_2():
    inp = open("test.in").readlines()

    maze = []
    s_pos = (-1, -1)

    for i in range(len(inp)):
        line = inp[i]
        if line.strip() != "":
            line_s = list(line.strip())
            maze.append(line_s)
            if "S" in line_s:
                j = line_s.index("S")
                s_pos = (i, j)

    curs = []
    visited = [s_pos]
    # steps = 1

    # check north:
    if s_pos[0] - 1 >= 0:
        i, j = s_pos[0] - 1, s_pos[1]
        if maze[i][j] == "|" or maze[i][j] == "7" or maze[i][j] == "F":
            curs.append((i, j))

    # check east:
    if len(curs) == 0 and s_pos[1] + 1 < len(maze[0]):
        i, j = s_pos[0], s_pos[1] + 1
        if maze[i][j] == "-" or maze[i][j] == "J" or maze[i][j] == "7":
            curs.append((i, j))

    # check south:
    if len(curs) == 0 and s_pos[0] + 1 < len(maze):
        i, j = s_pos[0] + 1, s_pos[1]
        if maze[i][j] == "|" or maze[i][j] == "J" or maze[i][j] == "L":
            curs.append((i, j))

    # check west:
    if len(curs) == 0 and s_pos[1] - 1 >= 0:
        i, j = s_pos[0], s_pos[1] - 1
        if maze[i][j] == "-" or maze[i][j] == "L" or maze[i][j] == "F":
            curs.append((i, j))

    while len(curs) != 0:
        next_curs = []
        for cur in curs:
            poss = []
            i, j = cur[0], cur[1]
            if maze[i][j] == "|":
                poss = [(i - 1, j), (i + 1, j)]
            elif maze[i][j] == "-":
                poss = [(i, j - 1), (i, j + 1)]
            elif maze[i][j] == "L":
                poss = [(i - 1, j), (i, j + 1)]
            elif maze[i][j] == "J":
                poss = [(i, j - 1), (i - 1, j)]
            elif maze[i][j] == "7":
                poss = [(i, j - 1), (i + 1, j)]
            elif maze[i][j] == "F":
                poss = [(i, j + 1), (i + 1, j)]

            if poss[0] not in visited:
                next_curs.append(poss[0])
            elif poss[1] not in visited:
                next_curs.append(poss[1])

            visited.append(cur)
            # print(visited)
            # print(next_curs)

        curs = next_curs
        # steps += 1

    area_up_inc = 0
    area_up_ex = 0

    j = len(visited) - 1
    for i in range(len(visited)):
        if visited[j][0] - visited[i][0] > 0:
            area_up_inc += (visited[i][1] + 1) * (visited[j][0] - visited[i][0])
            area_up_ex += visited[i][1] * (visited[j][0] - visited[i][0])
        elif visited[j][0] - visited[i][0] < 0:
            area_up_inc += visited[i][1] * (visited[j][0] - visited[i][0])
            area_up_ex += (visited[i][1] + 1) * (visited[j][0] - visited[i][0])
        j = i
        print(area_up_inc)

    print(min(abs(area_up_inc), abs(area_up_ex)))


def main():
    part_2()


if __name__ == '__main__':
    main()