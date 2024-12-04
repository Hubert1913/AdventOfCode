def main():
    inp = open("data.in").readlines()

    table = []
    for line in inp:
        if line.strip() != "":
            table.append(list(line.strip()))

    n = len(table)

    goal = [['X', 'M', 'A', 'S'], ['S', 'A', 'M', 'X']]
    total = 0

    for i in range(n):
        for j in range(n-3):
            if (table[i][j:j+4]) in goal:
                total += 1

    for i in range(n-3):
        for j in range(n):
            if list(map(lambda x: x[j], table[i:i+4])) in goal:
                total += 1

    for i in range(n-3):
        x = 0
        y = i
        while x < n-3 and y < n-3:
            if [table[y+j][x+j] for j in range(4)] in goal:
                total += 1
            x += 1
            y += 1

    for i in range(1, n-3):
        x = i
        y = 0
        while x < n-3 and y < n-3:
            if [table[y+j][x+j] for j in range(4)] in goal:
                total += 1
            x += 1
            y += 1

    for i in range(n - 3):
        x = n-1
        y = i
        while x >= 3 and y < n-3:
            if [table[y + j][x - j] for j in range(4)] in goal:
                total += 1
            x -= 1
            y += 1

    for i in range(3, n-1):
        x = i
        y = 0
        while x >= 3 and y < n - 3:
            if [table[y + j][x - j] for j in range(4)] in goal:
                total += 1
            x -= 1
            y += 1

    print(total)


def main_part_2():
    inp = open("data.in").readlines()

    table = []
    for line in inp:
        if line.strip() != "":
            table.append(list(line.strip()))

    n = len(table)

    goal = [['M', 'A', 'S'], ['S', 'A', 'M']]
    total = 0

    for i in range(n-2):
        x = 0
        y = i
        while x < n-2 and y < n-2:
            if [table[y+j][x+j] for j in range(3)] in goal and [table[y+j][x+2-j] for j in range(3)] in goal:
                total += 1
            x += 1
            y += 1

    for i in range(1, n-2):
        x = i
        y = 0
        while x < n-2 and y < n-2:
            if [table[y+j][x+j] for j in range(3)] in goal and [table[y+j][x+2-j] for j in range(3)] in goal:
                total += 1
            x += 1
            y += 1

    print(total)


if __name__ == '__main__':
    # main()
    main_part_2()