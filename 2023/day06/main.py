

def main():
    inp = open("data.in").readlines()

    times = inp[0].split(":")[1].strip().split()
    time = ""
    for t in times:
        time += t
    time = int(time)

    dists = inp[1].split(":")[1].strip().split()
    dist = ""
    for d in dists:
        dist += d
    dist = int(dist)

    # choices = []

    # for i in range(len(times)):
    #     t = times[i]
    #     d = dist[i]
    #     cur_choi = 0
    choices = 0
    for j in range(int(dist/time), time):
        if (time-j) * j > dist:
            choices += 1
    # choices.append(cur_choi)

    # total = 1 # bad but works lmao
    # for c in choices:
    #     total *= c

    print(choices)

    # total = 0
    # for line in inp:
    #     if line.strip() != "":
    #         id, r, g, b = get_data(line.strip())
    #         # total += is_valid(id, r, g, b)
    #         total += mult(r, g, b)
    #
    # print(total)


if __name__ == '__main__':
    main()