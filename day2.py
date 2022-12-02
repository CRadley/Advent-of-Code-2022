VALUES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

MAPPINGS = {
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
    if VALUES[move[1]] == VALUES[move[0]]:
        return 3 + VALUES[move[1]]
    elif any(move == wm for wm in (["C", "X"], ["A", "Y"], ["B", "Z"])):
        return 6 + VALUES[move[1]]
    return VALUES[move[1]]


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_moves(file_input: str):
    return [line.split(" ") for line in file_input.split("\n")]


def determine_player_score(moves) -> int:
    scores = [determine_move_score(move) for move in moves]
    return sum(scores)


def determine_part_two_score(move) -> int:
    return MAPPINGS[move]


def part_two(moves) -> int:
    scores = [determine_part_two_score(tuple(move)) for move in moves]
    return sum(scores)


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day2.txt")
    moves = determine_moves(file_input)
    print(determine_player_score(moves))
    print(part_two(moves))


if __name__ == "__main__":
    main()
