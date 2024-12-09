

def main():
    inp = open("data.in").readlines()

    inp = inp[0].strip()

    data = []
    ind = 0
    free = False
    for char in inp:
        for i in range(int(char)):
            if free:
                data.append(".")
            else:
                data.append(ind)
        if free:
            ind += 1

        free = not free

    end = len(data) - 1
    start = 0
    while data[end] != 0:
        if start < len(data) and data[start] != ".":
            start += 1
        elif data[end] == ".":
            end -= 1
        else:
            num = data[end]
            ind = end
            while data[ind] == num:
                ind -= 1
            length_file = end - ind
            length_empty = 0

            while length_empty < length_file and start < len(data):
                ind_s = start
                while ind_s < len(data) and data[ind_s] == ".":
                    ind_s += 1
                length_empty = ind_s - start
                if length_empty < length_file and start < len(data):
                    start = ind_s
                    while start < len(data) and data[start] != ".":
                        start += 1

            if length_empty >= length_file and start < end:
                for i in range(length_file):
                    data[start] = data[end]
                    data[end] = "."
                    start += 1
                    end -= 1
                start = 0
            else:
                while data[end] == num or data[end] == ".":
                    end -= 1
                start = 0

    total = 0
    for i in range(len(data)):
        if data[i] != ".":
            total += i * data[i]
    print(total)


if __name__ == '__main__':
    main()