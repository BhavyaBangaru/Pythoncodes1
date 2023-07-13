def print_formatted(num):
    b = bin(num)
    l = len(b) - 2
    for i in range(1, num + 1):
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
        o = oct(i)[2:]
        print(str(i).rjust(l), o.rjust(l), h.rjust(l), b.rjust(l))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)