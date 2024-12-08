import math


def main():
    inp = open("data.in").readlines()

    antennas = {}
    for i in range(len(inp)):
        line = inp[i]
        if line.strip() != "":
            for j in range(len(list(line.strip()))):
                char = list(line.strip())[j]
                if char != ".":
                    if char not in antennas:
                        antennas[char] = [(j, i)]
                    else:
                        antennas[char].append((j, i))
    m = len(inp)
    n = len(inp[0].strip())
    anti = set()
    for char in antennas:
        ants = antennas[char]
        for i in range(len(ants)):
            for j in range(i+1, len(ants)):
                first = ants[i]
                second = ants[j]
                diff = (second[0] - first[0], second[1] - first[1])
                g = math.gcd(diff[0], diff[1])
                diff = (diff[0] / g, diff[1] / g)
                # l = (second[0] + diff[0], second[1] + diff[1])
                # if n > l[0] >= 0 and 0 <= l[1] < m:
                #     anti.add(l)
                # h = (first[0] - diff[0], first[1] - diff[1])
                # if n > h[0] >= 0 and m > h[1] >= 0:
                #     anti.add(h)
                anti.add(first)
                pos = first
                pos = (pos[0] + diff[0], pos[1] + diff[1])
                while n > pos[0] >= 0 and m > pos[1] >= 0:
                    anti.add(pos)
                    pos = (pos[0] + diff[0], pos[1] + diff[1])

                pos = first
                pos = (pos[0] - diff[0], pos[1] - diff[1])
                while n > pos[0] >= 0 and m > pos[1] >= 0:
                    anti.add(pos)
                    pos = (pos[0] - diff[0], pos[1] - diff[1])

    print(len(anti))


if __name__ == '__main__':
    main()