
def main():
    inp = open("data.in").read()
    data = []

    for machine in inp.split("\n\n"):
        parts = machine.split("\n")
        info = []
        for i in range(2):
            p = parts[i]
            p = p.split(": ")[1].split(", ")
            info.append(list(map(lambda x: int(x.split("+")[1]), p)))
        p = parts[2]
        p = p.split(": ")[1].split(", ")
        info.append(list(map(lambda x: 10000000000000 + int(x.split("=")[1]), p)))
        data.append(info)

    total = 0
    for machine in data:
        a = machine[0]
        b = machine[1]
        goal = machine[2]
        min_a = 0
        if goal[0] - 100 * b[0] > 0:
            min_a = (goal[0] - 100 * b[0]) // a[0]
        if goal[1] - 100 * b[1] > 0:
            min_a = max(min_a, (goal[1] - 100 * b[1]) // a[1])

        max_a = min(goal[0] // a[0], goal[1] // a[1])

        cost = 0
        for i in range(min_a, max_a+1):
            diff_x = goal[0] - i * a[0]
            if diff_x % b[0] == 0:
                num_b = int(diff_x / b[0])
                if num_b * b[1] + i * a[1] == goal[1]:
                    cost = min(cost, num_b + 3*i) if cost != 0 else num_b + 3*i
        total += cost
    print(total)
    # dont know how to do part 2 :(


if __name__ == '__main__':
    main()
