def test(target, nums):
    if nums[0] > target:
        return False
    if len(nums) == 1:
        return nums[0] == target

    ret = False
    ret = ret or test(target, [nums[0] + nums[1]] + nums[2:])
    ret = ret or test(target, [nums[0] * nums[1]] + nums[2:])
    length = len(str(nums[1]))
    ret = ret or test(target, [nums[0] * 10**length + nums[1]] + nums[2:])

    return ret


def main():
    inp = open("data.in").readlines()

    data = []
    for line in inp:
        if line.strip() != "":
            data.append(list(map(lambda x: int(x), line.replace(":", "").split())))

    total = 0
    for row in data:
        if test(row[0], row[1:]):
            total += row[0]

    print(total)


if __name__ == '__main__':
    main()