from collections import deque


def main():
    inp = open("data.in").readlines()

    grid = []
    goal = (0, 0)

    shortcut_goal = 100

    for i, line in enumerate(inp):
        if line.strip() != "":
            row = []
            for j, char in enumerate(line.strip()):
                if char == '#':
                    row.append(-1)
                elif char == 'E':
                    goal = (i, j)
                    row.append(0)
                else:
                    row.append(-10)
            grid.append(row)

    n = len(grid)
    m = len(grid[0])

    dirs = [-1, 0, 1, 0, -1]
    que = deque()
    que.append(goal)
    while len(que) > 0:
        cur = que.popleft()
        cur_dist = grid[cur[0]][cur[1]]
        for i in range(4):
            np = (cur[0] + dirs[i], cur[1] + dirs[i+1])
            if np[0] < 0 or np[0] >= n or np[1] < 0 or np[1] >= m:
                continue
            od = grid[np[0]][np[1]]
            if od == -1:
                continue
            if od == -10 or od > cur_dist + 1:
                grid[np[0]][np[1]] = cur_dist + 1
                que.append(np)

    counter = 0

    xs = [-2, -1, 0, 1, 2, 1, 0, -1]
    ys = [0, 1, 2, 1, 0, -1, -2, -1]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dist = grid[i][j]
            if dist == -1:
                continue
            for dx in range(41):
                for dy in range(41):
                    np = (i + dx - 20, j + dy - 20)
                    if np[0] < 0 or np[0] >= n or np[1] < 0 or np[1] >= m:
                        continue
                    manhattan = (abs(dx - 20) + abs(dy - 20))
                    if manhattan > 20:
                        continue
                    od = grid[np[0]][np[1]]
                    if od == -1:
                        continue
                    nc = dist + manhattan
                    diff = od - nc
                    if diff >= shortcut_goal:
                        counter += 1

            # for d in range(8):
            #     np = (i + xs[d], j + ys[d])
            #     if np[0] < 0 or np[0] >= n or np[1] < 0 or np[1] >= m:
            #         continue
            #     od = grid[np[0]][np[1]]
            #     if od == -1:
            #         continue
            #     nc = dist + 2
            #     diff = od - nc
            #     if diff >= shortcut_goal:
            #         counter += 1

    print(counter)


if __name__ == '__main__':
    main()
