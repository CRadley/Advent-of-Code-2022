MOVE_VALUES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

PART_TWO_CHEAT_SHEET = {
    ("A", "X"): 3,
    ("A", "Y"): 4,
    ("A", "Z"): 8,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7,
}


def determine_move_score(move):
    if MOVE_VALUES[move[1]] == MOVE_VALUES[move[0]]:
        return 3 + MOVE_VALUES[move[1]]
    elif any(move == wm for wm in (("C", "X"), ("A", "Y"), ("B", "Z"))):
        return 6 + MOVE_VALUES[move[1]]
    return MOVE_VALUES[move[1]]


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_moves(file_input: str):
    return [tuple(line.split(" ")) for line in file_input.split("\n")]


def part_one(moves) -> int:
    return sum([determine_move_score(move) for move in moves])


def part_two(moves) -> int:
    return sum([PART_TWO_CHEAT_SHEET[move] for move in moves])


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day2.txt")
    moves = determine_moves(file_input)
    print(part_one(moves))
    print(part_two(moves))


if __name__ == "__main__":
    main()
