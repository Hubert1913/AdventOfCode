import re


def main():
    inp = open("data.in").readlines()

    data = "".join(inp)

    regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))"
    enabled = True

    parts = re.findall(regex, data)

    total = 0
    for part in parts:
        if part[3] != "":
            enabled = False
        elif part[2] != "":
            enabled = True
        elif enabled:
            total += int(part[0]) * int(part[1])

    print(total)

if __name__ == '__main__':
    main()