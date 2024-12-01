from functools import cmp_to_key
letters = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
let_map = {}

for i in range(len(letters)):
    let_map[letters[i]] = i


def get_strength(hand):
    cards = {"J": 0}
    for char in hand:
        if char not in cards:
            cards[char] = 1
        else:
            cards[char] += 1

    sort = sorted(cards.values())
    max_c = sort[-1]
    if max_c != 5:
        sec_max = sort[-2]

    s = 0
    if max_c == 5:
        s = 7
    elif max_c == 4:
        s = 6
        if cards["J"] == 1 or cards["J"] == 4:
            s = 7
    elif max_c == 3 and sec_max == 2:
        s = 5
        if cards["J"] == 2 or cards["J"] == 3:
            s = 7
    elif max_c == 3 and sec_max == 1:
        s = 4
        if cards["J"] == 1 or cards["J"] == 3:
            s = 6
    elif max_c == 2 and sec_max == 2:
        s = 3
        if cards["J"] == 2:
            s = 6
        if cards["J"] == 1:
            s = 5
    elif max_c == 2 and sec_max == 1:
        s = 2
        if cards["J"] == 1 or cards["J"] == 2:
            s = 4
    elif max_c == 1:
        s = 1
        if cards["J"] == 1:
            s = 2

    return s


def parse_line(line):
    spl = line.split()
    return spl[0], get_strength(spl[0]), int(spl[1])


def compare(item1, item2):
    global let_map
    if item1[1] != item2[1]:
        return item1[1] - item2[1]
    else:
        for i in range(5):
            if item1[0][i] != item2[0][i]:
                return let_map[item2[0][i]] - let_map[item1[0][i]]


def main():
    inp = open("data.in").readlines()

    full_data = []
    for line in inp:
        if line.strip() != "":
            hand, stre, bid = parse_line(line.strip())
            full_data.append((hand, stre, bid))

    sort = sorted(full_data, key=cmp_to_key(compare))

    total = 0
    for i in range(len(sort)):
        total += (i + 1) * sort[i][2]

    print(total)


if __name__ == '__main__':
    main()