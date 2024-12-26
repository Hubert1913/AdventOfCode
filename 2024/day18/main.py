from collections import deque


def main():
    num = 1024
    max_num = 3450
    # apparently brute forcing it works lol
    while num < max_num:
        num += 1
        inp = open("data.in").readlines()

        size = 71
        # num = 1024
        data = [[0 for _ in range(size)] for _ in range(size)]
        for k, line in enumerate(inp):
            if k == num:
                break
            if line.strip() != "":
                l = [int(x) for x in line.split(",")]
                data[l[1]][l[0]] = 1

        visited = set()
        que = deque()
        que.append((0, 0))
        visited.add((0, 0))
        goal = (size-1, size-1)
        dirs = [1, 0, -1, 0, 1]
        length = -1
        next_que = deque()
        found = False

        while len(que) > 0:
            length += 1
            while len(que) > 0:
                cur = que.popleft()
                if cur == goal:
                    found = True
                    break
                for i in range(4):
                    next_pos = (cur[0] + dirs[i], cur[1] + dirs[i+1])
                    if 0 <= next_pos[0] < size and 0 <= next_pos[1] < size:
                        if data[next_pos[0]][next_pos[1]] == 1 or next_pos in visited:
                            continue
                        next_que.append(next_pos)
                        visited.add(next_pos)

            que = next_que
            next_que = deque()

            if found:
                break

        if not found:
            print(inp[num-1])
            break
    # print(length)


if __name__ == '__main__':
    main()