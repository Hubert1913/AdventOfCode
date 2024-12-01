from math import lcm


def parse_graph(lines):
    g = {}
    for line in lines:
        spl = line.split(" = ")
        g[spl[0]] = spl[1][1:-1].split(", ")
    return g


def get_steps_num(start, g, steps):
    num = 0
    cur3 = start
    while cur3[2] != "Z":
        if steps[num % len(steps)] == "L":
            cur3 = g[cur3][0]
        else:
            cur3 = g[cur3][1]
        num += 1
    return num


def main():
    inp = open("data.in").readlines()
    steps = inp[0].strip()

    lines = []
    for line in inp[2:]:
        if line.strip() != "":
            lines.append(line.strip())

    g = parse_graph(lines)

    curs = list(filter(lambda k: k[2] == "A", g.keys()))
    lens = []
    for cur in curs:
        lens.append(get_steps_num(cur, g, steps))

    print(lcm(*lens))


if __name__ == '__main__':
    main()