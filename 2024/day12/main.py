from collections import deque


def run_bfs(pos: (int, int), visited: set, data):
    letter = data[pos[0]][pos[1]]
    que = deque()
    que.append(pos)
    dirs = [1, 0, -1, 0, 1]
    per = 0
    area = 0
    # visited.add(pos)
    sides = set()

    while len(que) != 0:
        cur = que.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        area += 1

        for i in range(4):
            next_pos = (cur[0] + dirs[i], cur[1] + dirs[i+1])
            if 0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0]):
                if data[next_pos[0]][next_pos[1]] == letter:
                    if next_pos not in visited:
                        que.append(next_pos)
                        # visited.add(next_pos)
                        # area += 1
                else:
                    # already_in = False
                    # if dirs[i] == 0:
                    #     if 0 <= cur[0] - 1:
                    #         already_in = already_in or (data[cur[0]-1][cur[1]] == letter and data[next_pos[0]-1][next_pos[1]] != letter and (cur[0]-1, cur[1]) in visited)
                    #     if cur[0] + 1 < len(data):
                    #         already_in = already_in or (data[cur[0]+1][cur[1]] == letter and data[next_pos[0]+1][next_pos[1]] != letter and (cur[0]+1, cur[1]) in visited)
                    # else:
                    #     if 0 <= cur[1] - 1:
                    #         already_in = already_in or (data[cur[0]][cur[1]-1] == letter and data[next_pos[0]][next_pos[1]-1] != letter and (cur[0], cur[1]-1) in visited)
                    #         # if cur == (1, 5):
                    #         #     print(data[cur[0]][cur[1]-1] == letter)
                    #         #     print(data[next_pos[0]][next_pos[1]-1] != letter)
                    #         #     print((next_pos[0], next_pos[1]-1))
                    #         #     print((cur[0], cur[1]-1) in visited)
                    #         #     print(already_in)
                    #     if cur[1] + 1 < len(data[0]):
                    #         already_in = already_in or (data[cur[0]][cur[1]+1] == letter and data[next_pos[0]][next_pos[1]+1] != letter and (cur[0], cur[1]+1) in visited)
                    #         # if cur == (1, 5):
                    #         #     print(already_in)
                    # if not already_in:
                    #     print(f"{cur}, ({dirs[i]},{dirs[i+1]})")
                    #     # print(visited)
                    #     per += 1
                    sides.add((cur[0], cur[1], dirs[i], dirs[i+1]))
            else:
                # already_in = False
                # if dirs[i] == 0:
                #     if 0 <= cur[0] - 1:
                #         already_in = already_in or (data[cur[0] - 1][cur[1]] == letter and (cur[0] - 1, cur[1]) in visited)
                #     if cur[0] + 1 < len(data):
                #         already_in = already_in or (data[cur[0] + 1][cur[1]] == letter and (cur[0] + 1, cur[1]) in visited)
                # else:
                #     if 0 <= cur[1] - 1:
                #         already_in = already_in or (data[cur[0]][cur[1] - 1] == letter and (cur[0], cur[1] - 1) in visited)
                #     if cur[1] + 1 < len(data[0]):
                #         already_in = already_in or (data[cur[0]][cur[1] + 1] == letter and (cur[0], cur[1] + 1) in visited)
                # if not already_in:
                #     print(f"{cur}, ({dirs[i]},{dirs[i + 1]})")
                #     per += 1
                # per += 1
                sides.add((cur[0], cur[1], dirs[i], dirs[i + 1]))

    sides = {(x, y, dx, dy) for x, y, dx, dy in sides if (x-abs(dy), y-abs(dx), dx, dy) not in sides}
    per = len(sides)

    return area, per


def main():
    inp = open("data.in").readlines()

    data = []
    for line in inp:
        if line.strip() != "":
            data.append(list(line.strip()))

    n = len(data)
    m = len(data[0])

    visited = set()

    total = 0

    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                a, p = run_bfs((i, j), visited, data)
                total += a * p

    print(total)




if __name__ == '__main__':
    main()