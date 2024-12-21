import png


def simulate(ps, vs, w, h):
    for i in range(len(ps)):
        ps[i] = simulate_one(ps[i], vs[i], w, h)


def simulate_one(pos, v, w, h):
    # for i in range(n):
    pos = ((pos[0] + v[0]) % w, (pos[1] + v[1]) % h)

    # if data[pos[1]][pos[0]] == 0:
    #     data[pos[1]][pos[0]] = 1
    return pos

    # if pos[0] < w//2:
    #     if pos[1] < h//2:
    #         return 1, 0, 0, 0
    #     elif pos[1] > h//2:
    #         return 0, 1, 0, 0
    #     else:
    #         return 0, 0, 0, 0
    # elif pos[0] > w//2:
    #     if pos[1] < h//2:
    #         return 0, 0, 1, 0
    #     elif pos[1] > h//2:
    #         return 0, 0, 0, 1
    #     else:
    #         return 0, 0, 0, 0
    # else:
    #     return 0, 0, 0, 0


def main():
    inp = open("data.in").readlines()
    w = 101
    h = 103

    # q1 = 0
    # q2 = 0
    # q3 = 0
    # q4 = 0

    ps = []
    vs = []

    for line in inp:
        if line.strip() != "":
            parts = line.split(" v=")
            p = parts[0].split("p=")[1].split(",")
            p = (int(p[0]), int(p[1]))
            v = parts[1].split(",")
            v = (int(v[0]), int(v[1]))
            ps.append(p)
            vs.append(v)

            # simulate(p, v, w, h, 100, data)
            # a, b, c, d = simulate(p, v, w, h, 100, data)
            # q1 += a
            # q2 += b
            # q3 += c
            # q4 += d

    # print(q1 * q2 * q3 * q4)

    for i in range(1, 10000):
        data = [[0 for _ in range(w)] for _ in range(h)]
        simulate(ps, vs, w, h)
        for p in ps:
            data[p[1]][p[0]] = 1

        palette = [(0x0, 0x00, 0x00), (0x00, 0xFF, 0x00)]
        with open(f'images/step_{i}.png', 'wb') as f:
            writer = png.Writer(w, h, palette=palette)
            writer.write(f, data)


if __name__ == '__main__':
    main()