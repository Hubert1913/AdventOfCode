

def main():
    inp = open("data.in").readlines()

    left = []
    right = []
    for line in inp:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    left = sorted(left)
    right = sorted(right)

    total = 0
    for i in range(len(left)):
        # total += abs(left[i] - right[i])
        total += left[i] * len(list(filter(lambda x: x == left[i], right)))
    print(total)


if __name__ == '__main__':
    main()