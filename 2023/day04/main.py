def get_points_for_card(winning, my):
    count = 0
    for num in my:
        if num in winning:
            count += 1

    # if count > 0:
    #     return 2 ** (count - 1)
    # else:
    #     return 0
    return count


def parse_line(line):
    first = line.split(": ")
    id = int(first[0].split()[1])
    nums = first[1].split(" | ")
    winning = nums[0].split()
    my = nums[1].split()

    return id, winning, my


def main():
    inp = open("data.in").readlines()
    totals = []
    for i in range(len(inp) + 1):
        totals.append(1)
    totals[0] = 0

    total = 0
    for line in inp:
        if line.strip() != "":
            id, winning, my = parse_line(line.strip())
            count = get_points_for_card(winning, my)
            # total += get_points_for_card(winning, my)
            for i in range(count):
                totals[id + i + 1] += totals[id]

    # print(totals)
    print(sum(totals))


if __name__ == '__main__':
    main()