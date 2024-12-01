
def find_nums(table):
    vert_len = len(table)
    hor_len = len(table[0])
    total = 0

    for i in range(vert_len):
        j = 0
        while j < hor_len:
            if table[i][j].isdigit():
                start = j
                while j < hor_len and table[i][j].isdigit():
                    j += 1
                flag = False
                for k in range(max(0, start-1), min(j+1, hor_len)):
                    if i > 0:
                        if (not table[i-1][k].isdigit()) and table[i-1][k] != '.':
                            flag = True
                    if (not table[i][k].isdigit()) and table[i][k] != '.':
                        flag = True
                    if i < vert_len - 1:
                        if (not table[i+1][k].isdigit()) and table[i+1][k] != '.':
                            flag = True
                    if flag:
                        break
                if not flag:
                    continue

                num = ""
                for z in range(start, j):
                    num += table[i][z]
                num = int(num)
                # print(num)
                total += num

            else:
                j += 1

    return total


def find_gears(table):
    vert_len = len(table)
    hor_len = len(table[0])
    gears = {}


    for i in range(vert_len):
        j = 0
        while j < hor_len:
            if table[i][j].isdigit():
                start = j
                while j < hor_len and table[i][j].isdigit():
                    j += 1
                # flag = False
                adj_gears = []
                for k in range(max(0, start-1), min(j+1, hor_len)):
                    if i > 0:
                        if table[i-1][k] == '*':
                            adj_gears.append((i-1, k))
                    if table[i][k] == '*':
                        adj_gears.append((i, k))
                    if i < vert_len - 1:
                        if table[i + 1][k] == '*':
                            adj_gears.append((i + 1, k))

                if len(adj_gears) == 0:
                    continue

                num = ""
                for z in range(start, j):
                    num += table[i][z]
                num = int(num)
                for coords in adj_gears:
                    if coords not in gears:
                        gears[coords] = []
                    gears[coords].append(num)

            else:
                j += 1

    total = 0
    # print(gears)

    for gear in gears:
        if len(gears[gear]) == 2:
            total += gears[gear][0] * gears[gear][1]

    return total


def main():
    inp = open("data.in").readlines()

    total = 0
    table = []
    for line in inp:
        if line.strip() != "":
            table.append(list(line.strip()))
    #         # total += is_valid(id, r, g, b)
    #         total += mult(r, g, b)

    total = find_gears(table)
    print(total)


if __name__ == '__main__':
    main()