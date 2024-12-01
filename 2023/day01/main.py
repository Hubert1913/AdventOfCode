
def find_num(line):
    first = -1
    f_ind = len(line)
    last = -1
    l_ind = -1
    for i, char in enumerate(line):
        if char.isdigit():
            if first == -1:
                first = int(char)
                f_ind = i
                last = int(char)
                l_ind = i
            else:
                last = int(char)
                l_ind = i

    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    cur = 1
    for num in nums:
        indf = line.find(num)
        indl = line.rfind(num)
        if indf == -1:
            cur += 1
            continue

        if indf < f_ind:
            f_ind = indf
            first = cur

        if indl > l_ind:
            l_ind = indl
            last = cur

        cur += 1

    return first * 10 + last


def main():
    inp = open("data.in").readlines()

    total = 0
    for line in inp:
        if line.strip() != "":
            total += find_num(line)

    print(total)


if __name__ == '__main__':
    main()