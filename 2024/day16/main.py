from queue import PriorityQueue
from collections import deque


def main():
    inp = open("data.in").readlines()

    data = []
    start = (0,0)
    end = (0,0)
    for i, line in enumerate(inp):
        if line.strip() != "":
            data.append([])
            for j, char in enumerate(list(line)):
                if char == "#":
                    data[i].append(1)
                elif char == "S":
                    start = (i, j)
                    data[i].append(0)
                elif char == "E":
                    end = (i, j)
                    data[i].append(0)
                else:
                    data[i].append(0)

    dirs = {
        1: [0, 1],
        2: [1, 0],
        3: [0, -1],
        4: [-1, 0]
    }
    best = {(start, 1): 0}
    pq = PriorityQueue()
    pq.put((0, (start, 1)))
    lowest = 0

    while pq.qsize() > 0:
        cur = pq.get()
        cost = cur[0]
        pos = cur[1][0]
        d_orig = cur[1][1]
        if (pos, d_orig) in best and cost > best[(pos, d_orig)]:
            continue
        if pos == end:
            lowest = cost
            break
        for di in dirs:
            d = dirs[di]
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if data[new_pos[0]][new_pos[1]] == 0:
                diff = abs(d_orig - di)
                if diff == 3:
                    diff = 1
                new_cost = cost + 1 + 1000 * diff
                pq.put((new_cost, (new_pos, di)))
                if ((new_pos, di) not in best) or new_cost <= best[(new_pos, di)]:

                    best[(new_pos, di)] = new_cost

    que = deque()
    for d in dirs:
        if (end, d) in best and best[(end, d)] == lowest:
            que.append((end, d))
    visited = set()

    while len(que) > 0:
        cur = que.popleft()
        pos = cur[0]
        visited.add(pos)
        d_orig = cur[1]
        cost = best[cur]
        d_op = [-dirs[d_orig][0], -dirs[d_orig][1]]
        p_pos = (pos[0] + d_op[0], pos[1] + d_op[1])
        for d in dirs:
            diff = abs(d_orig - d)
            diff = diff if diff != 3 else 1
            p_cost = cost - 1 - diff * 1000
            if (p_pos, d) in best and best[(p_pos, d)] == p_cost:
                que.append((p_pos, d))

    print(len(visited))


if __name__ == '__main__':
    main()