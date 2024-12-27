def valid(pats, goal, invalid, known):
    if goal == "":
        return True
    if goal in invalid:
        return False
    if goal in known:
        return known[goal]

    out = 0

    for p in pats:
        if len(p) > len(goal):
            continue

        fits = True
        for k, char in enumerate(p):
            if char != goal[k]:
                fits = False
                break
        if fits:
            out += valid(pats, goal[len(p):], invalid, known)
        # if out:
        #     break

    if out == 0:
        invalid.add(goal)
    else:
        known[goal] = out

    return out


def main():
    inp = open("data.in").read().split("\n\n")

    pats = inp[0].split(", ")
    invalid = set()
    known = {}

    total = 0
    for des in inp[1].split("\n"):
        # if valid(pats, des, invalid, known):
            # total += 1
        total += valid(pats, des, invalid, known)

    print(total)


if __name__ == '__main__':
    main()