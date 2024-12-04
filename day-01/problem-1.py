#! /bin/python3

def main():
    list_a = []
    list_b = []

    while True:
        try:
            [a, b] = [int(x) for x in input().split()]
            list_a.append(a)
            list_b.append(b)
        except EOFError:
            break

    list_a.sort()
    list_b.sort()

    acc = 0
    for i in range(len(list_a)):
        acc += abs(list_a[i] - list_b[i])
    print(acc)


if __name__ == "__main__":
    main()
