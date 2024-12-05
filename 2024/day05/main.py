

def main():
    inp = open("data.in").readlines()

    rules = {}
    orders = []
    rule_sec = True
    for line in inp:
        if line == "\n":
            rule_sec = False
        elif rule_sec:
            d = line.split("|")
            if int(d[0]) not in rules:
                rules[int(d[0])] = [int(d[1])]
            else:
                rules[int(d[0])].append((int(d[1])))
        else:
            orders.append(list(map(lambda x: int(x), line.split(","))))

    total = 0
    total_inc = 0

    for order in orders:
        prev = set()
        correct = True
        for o in order:
            if o in rules:
                for x in rules[o]:
                    if x in prev:
                        correct = False
                        break
            prev.add(o)
            if not correct:
                break
        if correct:
            total += order[int((len(order) - 1)/2)]
        else:
            changed = True
            fixed_order = order
            while changed:
                fo = fixed_order
                fo_c = []
                changed = False
                for i in range(len(fo)):
                    if fo[i] not in rules:
                        fo_c.append(fo[i])
                        continue
                    ind = None
                    for j in range(i):
                        if fo[j] in rules[fo[i]]:
                            ind = j
                            break
                    if ind is None:
                        fo_c.append(fo[i])
                        continue

                    fo_c.insert(ind, fo[i])
                    changed = True
                # print(fo)
                fixed_order = fo_c

            # print(fixed_order)
            total_inc += fixed_order[int((len(order) - 1)/2)]

    print(total)
    print(total_inc)




if __name__ == '__main__':
    main()