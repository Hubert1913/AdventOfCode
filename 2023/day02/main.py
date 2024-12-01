
def get_data(line):
    spl = line.split(": ")
    id = int(spl[0].split(" ")[1])
    subsets = spl[1].split("; ")
    counts = []
    for sub in subsets:
        counts.extend(sub.split(", "))

    r = 0
    g = 0
    b = 0
    for count in counts:
        data = count.split()
        if data[1] == "red":
            r = max(r, int(data[0]))
        elif data[1] == "green":
            g = max(g, int(data[0]))
        elif data[1] == "blue":
            b = max(b, int(data[0]))

    return id, r, g, b


def mult(r, g, b):
    return r * g * b


def is_valid(id, r, g, b):
    if r <=12 and g <= 13 and b <= 14:
        return id
    else:
        return 0


def main():
    inp = open("data.in").readlines()

    total = 0
    for line in inp:
        if line.strip() != "":
            id, r, g, b = get_data(line.strip())
            # total += is_valid(id, r, g, b)
            total += mult(r, g, b)

    print(total)


if __name__ == '__main__':
    main()