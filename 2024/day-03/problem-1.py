#! /bin/python3

import re

def main():
    acc = 0
    while True:
        try:
            line = input()
            #instances = re.findall(r"mul", line)
            instances = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
            for instance in instances:
                [a, b] = [ int(n) for n in instance[len("mul("):-1].split(",") ]
                acc += a * b
        except EOFError:
            break
    print(acc)

if __name__ == "__main__":
    main()