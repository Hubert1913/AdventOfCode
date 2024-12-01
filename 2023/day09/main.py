def parse_line(line):
    return list(map(lambda x: int(x), line.split()))


def extrapolate(line):
    lines = [line]
    flag = len(list(filter(lambda x: x != 0, line))) != 0

    while flag:
        new_line = []
        flag = False
        for i in range(len(line) - 1):
            num = line[i+1] - line[i]
            new_line.append(num)
            if num != 0:
                flag = True

        lines.append(new_line)
        line = new_line

    l = len(lines)
    for i in range(2, len(lines)+1):
        lines[l-i].append(lines[l-i][-1] + lines[l-i+1][-1])

    return lines[0][-1]


def extrapolate_back(line):
    line.reverse()
    lines = [line]
    flag = len(list(filter(lambda x: x != 0, line))) != 0

    while flag:
        new_line = []
        flag = False
        for i in range(len(line) - 1):
            num = line[i] - line[i+1]
            new_line.append(num)
            if num != 0:
                flag = True

        lines.append(new_line)
        line = new_line

    l = len(lines)
    for i in range(2, len(lines)+1):
        lines[l-i].append(lines[l-i][-1] - lines[l-i+1][-1])

    return lines[0][-1]


def main():
    inp = open("data.in").readlines()

    total = 0
    for line in inp:
        if line.strip() != "":
            total += extrapolate_back(parse_line(line.strip()))

    print(total)


if __name__ == '__main__':
    main()
    