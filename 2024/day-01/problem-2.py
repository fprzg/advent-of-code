#! /bin/python3

def register_occurrence(arr, b) -> list:
    delta = b - len(arr)
    if delta > 0:
        arr = arr + [0] * (delta + 1)
         
    arr[b] = arr[b] + 1
    return arr

def main():
    list_a = []
    occurrences_b = [0] * 1000

    while True:
        try:
            [a, b] = [int(x) for x in input().split()]
            list_a.append(a)
            occurrences_b = register_occurrence(occurrences_b, b)
        except EOFError:
            break

    acc = 0
    for a in list_a:
        acc += occurrences_b[a] * a
    print(acc)


if __name__ == "__main__":
    main()