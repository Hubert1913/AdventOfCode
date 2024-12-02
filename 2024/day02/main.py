
def is_safe(report):
    diff = report[0] - report[1]

    if diff == 0:
        return False

    diff = diff / abs(diff)

    for i in range(len(report) - 1):
        d = report[i] - report[i + 1]
        if not (1 <= d * diff <= 3):
            return False
    return True


def is_safe_part_2(report):
    ret = is_safe(report)

    for i in range(len(report)):
        ret = ret or is_safe([report[j] for j in range(len(report)) if j != i])

    return ret


def main():
    inp = open("data.in").readlines()

    reports = []
    for line in inp:
        if line.strip() != "":
            reports.append(list(map(lambda x: int(x), line.split())))

    total = sum(list(map(lambda r: 1 if is_safe_part_2(r) else 0, reports)))

    print(total)


if __name__ == '__main__':
    main()