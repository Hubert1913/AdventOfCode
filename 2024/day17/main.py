def get_combo(op, a, b, c):
    if 0 <= op <= 3:
        return op
    elif op == 4:
        return a
    elif op == 5:
        return b
    else:
        return c


def part_1(def_a):
    inp = open("data.in").read().split("\n\n")
    reg = inp[0].split("\n")
    a = int(reg[0].split(": ")[1])
    b = int(reg[1].split(": ")[1])
    c = int(reg[2].split(": ")[1])

    program = list(map(lambda x: int(x), inp[1].split(": ")[1].split(",")))

    out = []
    a = def_a

    ins_pointer = 0

    while ins_pointer < len(program):
        ins = program[ins_pointer]
        op = program[ins_pointer + 1]

        if ins == 0:
            a = int(a // (2 ** get_combo(op, a, b, c)))
        elif ins == 1:
            b = b ^ op
        elif ins == 2:
            b = get_combo(op, a, b, c) % 8
        elif ins == 3:
            if a != 0:
                ins_pointer = op
                continue
        elif ins == 4:
            b = b ^ c
        elif ins == 5:
            out.append(get_combo(op, a, b, c) % 8)
        elif ins == 6:
            b = int(a // (2 ** get_combo(op, a, b, c)))
        else:
            c = int(a // (2 ** get_combo(op, a, b, c)))

        ins_pointer += 2

    return out


def main():
    inp = open("data.in").read().split("\n\n")

    program = list(map(lambda x: int(x), inp[1].split(": ")[1].split(",")))

    all_a = [0]
    for j in range(len(program)):
        all_a = [8*x for x in all_a]

        next_a = []
        for a in all_a:
            for i in range(8):
                out = part_1(a + i)
                if out == program[len(program) - len(out):]:
                    next_a.append(a + i)
        all_a = next_a

    print(all_a)


if __name__ == '__main__':
    main()


