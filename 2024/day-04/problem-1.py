#! /bin/python3

from enum import Enum

class Direction(Enum):
    VERTICAL = 0
    VERTICAL_BACKWARDS = 3
    HORIZONTAL = 1
    HORIZONTAL_BACKWARDS = 4
    BLTR_DIAGONAL = 5
    BLTR_DIAGONAL_BACKWARDS = 6
    TLBR_DIAGONAL = 7
    TLBR_DIAGONAL_BACKWARDS = 8

def get_pos(x, y, dir) -> []:
    new_x, new_y = -1, -1
    match dir:
        case Direction.VERTICAL:
            new_x, new_y = x, y+1
        case Direction.VERTICAL_BACKWARDS:
            new_x, new_y = x, y-1
        case Direction.HORIZONTAL:
            new_x, new_y = x+1, y
        case Direction.HORIZONTAL_BACKWARDS:
            new_x, new_y = x-1, y
        case Direction.BLTR_DIAGONAL:
            new_x, new_y = x+1, y+1
        case Direction.BLTR_DIAGONAL_BACKWARDS:
            new_x, new_y = x-1, y-1
        case Direction.TLBR_DIAGONAL:
            new_x, new_y = x+1, y-1
        case Direction.TLBR_DIAGONAL_BACKWARDS:
            new_x, new_y = x-1, y+1
    return new_x, new_y

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
            if c == "X":
                for dir in Direction:
                    search_queue.append([x, y, "M", dir])
            x += 1
        x = 0
        y += 1

    while len(search_queue):
        [x, y, letter, dir] = search_queue.pop(0)
        new_x, new_y = get_pos(x, y, dir)
        if letter_matches(new_x, new_y, letter):
            if letter == "M":
                search_queue.append([new_x, new_y, "A", dir])
            if letter == "A":
                search_queue.append([new_x, new_y, "S", dir])
            if letter == "S":
                xmas_ocurrences += 1
    print(xmas_ocurrences)


if __name__ == "__main__":
    main()