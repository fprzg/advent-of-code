#! /bin/python3

def check_report(arr) -> str:
    step = arr[1] - arr[0]
    if step == 0 or len(arr) < 2:
        return "unsafe"
    asc = True if step > 0 else False

    if asc:
        for i in range(len(arr) - 1):
            step = arr[i + 1] - arr[i]
            if not (step >= 1 and step <= 3):
                return "unsafe"
    else:
        for i in range(len(arr) - 1):
            step = arr[i + 1] - arr[i]
            if not (step >= -3 and step <= -1):
                return "unsafe"
    return "safe"

def main():
    unsafe = 0
    safe = 0

    while True:
        try:
            row = [ int(x) for x in input().split()]
            if check_report(row) == "safe":
                safe += 1
            else:
                safe_if_drop_one_level = False
                for i in range(len(row)):
                    row_clone = row.copy()
                    row_clone.pop(i)
                    if check_report(row_clone) == "safe":
                        safe_if_drop_one_level = True
                        safe += 1
                        break
                if not safe_if_drop_one_level:
                    unsafe += 1
        except EOFError:
            break
    print(safe)

if __name__ == "__main__":
    main()