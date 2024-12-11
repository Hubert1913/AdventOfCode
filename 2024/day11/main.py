def count(num, blinks, mem):
    if blinks == 0:
        return 1
    if (num, blinks) in mem:
        return mem[(num, blinks)]

    if num == 0:
        x = count(1, blinks-1, mem)
        mem[(num, blinks)] = x
        return x
    elif len(str(num)) % 2 == 0:
        n = len(str(num))
        x = count(int(str(num)[:int(n/2)]), blinks-1, mem)
        y = count(int(str(num)[int(n/2):]), blinks-1, mem)
        mem[(num, blinks)] = x + y
        return x + y
    else:
        x = count(num * 2024, blinks-1, mem)
        mem[(num, blinks)] = x
        return x


def main():
    inp = open("data.in").readlines()

    data = list(map(lambda x: int(x), inp[0].split(" ")))

    total = 0
    mem = {}

    for x in data:
        total += count(x, 75, mem)

    print(total)


if __name__ == '__main__':
    main()