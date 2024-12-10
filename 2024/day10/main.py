from collections import deque


def run_bfs(data, start):
    visited = set()
    visited.add(start)
    que = deque()
    que.append(start)
    dirs = [1, 0, -1, 0, 1]
    total = 0

    while len(que) > 0:
        cur = que.popleft()
        height = data[cur[0]][cur[1]]
        if height == 9:
            total += 1
            continue
        for i in range(4):
            pos = (cur[0] + dirs[i], cur[1] + dirs[i+1])
            if 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]) and data[pos[0]][pos[1]] == height + 1: #and pos not in visited:
                que.append(pos)
                # Apparently just removing 'visited' solves whole part 2 lol
                # visited.add(pos)

    return total


def main():
    inp = open("data.in").readlines()

    data = []
    for line in inp:
        if line.strip() != "":
            data.append(list(map(lambda x: int(x), list(line.strip()))))

    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                total += run_bfs(data, (i, j))

    print(total)


if __name__ == '__main__':
    main()