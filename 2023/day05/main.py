
def get_secondary_map(map_lines):
    sec_map = []
    for line in map_lines:
        dest, sour, ran = parse_map_line(line)
        sec_map.append([sour, dest, ran])

    return sec_map


def parse_map_line(line):
    sp = line.split()
    dest = int(sp[0])
    sour = int(sp[1])
    ran = int(sp[2])

    return dest, sour, ran


# def main():
#     inp = open("data.in").readlines()
#
#     seeds = list(map(lambda s: int(s), inp[0].strip().split(": ")[1].split()))
#     main_map = {}
#
#     for s in seeds:
#         main_map[s] = s
#
#     i = 2
#     while i < len(inp):
#         map_lines = []
#         i += 1
#         while i < len(inp) and inp[i] != "\n":
#             map_lines.append(inp[i].strip())
#             i += 1
#
#         second_map = get_secondary_map(map_lines)
#
#         for key in main_map:
#             sor = main_map[key]
#             des = sor
#             for j in range(len(second_map)):
#                 s = second_map[j][0]
#                 d = second_map[j][1]
#                 r = second_map[j][2]
#                 if s <= sor < s + r:
#                     des = d + (sor - s)
#                     break
#
#             # if main_map[key] in second_map:
#             #     main_map[key] = second_map[main_map[key]]
#             main_map[key] = des
#
#         i += 1
#
#     min_val = max(main_map.values())
#     # min_seed = 0
#     for key in main_map:
#         if main_map[key] <= min_val:
#             # min_seed = key
#             min_val = main_map[key]
#
#     print(min_val)

def main():
    inp = open("data.in").readlines()

    seeds = list(map(lambda s: int(s), inp[0].strip().split(": ")[1].split()))
    cur_ranges = []
    for i in range(0, len(seeds), 2):
        cur_ranges.append([seeds[i], seeds[i + 1]])


    maps = []

    i = 2
    while i < len(inp):
        map_lines = []
        i += 1
        while i < len(inp) and inp[i] != "\n":
            map_lines.append(inp[i].strip())
            i += 1

        maps.append(get_secondary_map(map_lines))
        i += 1

    for k in range(7):
        next_ranges = []
        i = 0
        second_map = maps[k]

        while i < len(cur_ranges):
            cur = cur_ranges[i]

            for j in range(len(second_map)):
                s = second_map[j][0]
                d = second_map[j][1]
                r = second_map[j][2]

                if s <= cur[0] < s + r:
                    if cur[0] + cur[1] > s + r:
                        cur_ranges.append([s + r, cur[0] + cur[1] - (s + r)])
                        cur[1] = s + r - cur[0]
                    next_ranges.append([d + (cur[0] - s), cur[1]])
                    cur[0] = -1
                    cur[1] = -1
                    break

                if cur[0] < s <= cur[0] + cur[1]:
                    cur_ranges.append([s, cur[0] + cur[1] - s])
                    cur[1] = s - cur[0]

            if cur[0] != -1:
                next_ranges.append(cur)
            i += 1

        cur_ranges = next_ranges

    min_val = min(list(map(lambda x: x[0], cur_ranges)))
    print(min_val)


if __name__ == '__main__':
    main()