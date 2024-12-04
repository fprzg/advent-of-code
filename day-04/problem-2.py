#! /bin/python3

from enum import Enum

class MSide(Enum):
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

def letter_matches(x, y, letter) -> bool:
    if not (y >= 0 and y < len(input_map)):
        return False
    if not (x >= 0 and x < len(input_map[y])):
        return False
    return input_map[y][x] == letter

def main():
    xmas_ocurrences = 0
    x, y = 0, 0

    search_queue = []

    global input_map
    with open("input.txt", "r") as f:
        data = f.read().split("\n")
        input_map = data

    for line in input_map:
        for c in line:
            if c == "A":
                search_queue.append([x, y])
            x += 1
        x = 0
        y += 1

    while len(search_queue):
        [x, y] = search_queue.pop(0)
        shape_a = (letter_matches(x+1, y+1, "M") and letter_matches(x+1, y-1, "M") and letter_matches(x-1, y-1, "S") and letter_matches(x-1, y+1, "S"))
        shape_b = (letter_matches(x+1, y+1, "S") and letter_matches(x+1, y-1, "M") and letter_matches(x-1, y-1, "M") and letter_matches(x-1, y+1, "S"))
        shape_c = (letter_matches(x+1, y+1, "S") and letter_matches(x+1, y-1, "S") and letter_matches(x-1, y-1, "M") and letter_matches(x-1, y+1, "M"))
        shape_d = (letter_matches(x+1, y+1, "M") and letter_matches(x+1, y-1, "S") and letter_matches(x-1, y-1, "S") and letter_matches(x-1, y+1, "M"))
            
        if shape_a or shape_b or shape_c or shape_d:
            xmas_ocurrences += 1
    print(xmas_ocurrences)


if __name__ == "__main__":
    main()