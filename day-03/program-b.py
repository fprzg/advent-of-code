#! /bin/python3

import re

def main():
    acc = 0
    ignore = False
    while True:
        try:
            line = input()
            instances = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
            for instance in instances:
                match instance:
                    case "don't()":
                        ignore = True
                    case "do()":
                        ignore = False
                    case _:
                        if not ignore:
                            [a, b] = [ int(n) for n in instance[len("mul("):-1].split(",") ]
                            acc += a * b
        except EOFError:
            break
    print(acc)

if __name__ == "__main__":
    main()