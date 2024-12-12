from collections import deque


def run_bfs(pos: (int, int), visited: set, data):
    letter = data[pos[0]][pos[1]]
    que = deque()
    que.append(pos)
    dirs = [1, 0, -1, 0, 1]
    per = 0
    area = 1
    visited.add(pos)

    while len(que) != 0:
        cur = que.popleft()
        for i in range(4):
            next_pos = (cur[0] + dirs[i], cur[1] + dirs[i+1])
            if 0 <= next_pos[0] < len(data) and 0 <= next_pos[1] < len(data[0]):
                if data[next_pos[0]][next_pos[1]] == letter:
                    if next_pos not in visited:
                        que.append(next_pos)
                        visited.add(next_pos)
                        area += 1
                else:
                    per += 1
            else:
                per += 1

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
                # print(data[i][j])
                # print(a)
                # print(p)
                total += a * p

    print(total)




if __name__ == '__main__':
    main()