MOVE_VALUES = {
    ("A", "X"): (4, 3),
    ("B", "X"): (1, 1),
    ("C", "X"): (7, 2),
    ("A", "Y"): (8, 4),
    ("B", "Y"): (5, 5),
    ("C", "Y"): (2, 6),
    ("A", "Z"): (3, 8),
    ("B", "Z"): (9, 9),
    ("C", "Z"): (6, 7),
}

def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_moves(file_input: str):
    return [tuple(line.split(" ")) for line in file_input.split("\n")]

def determine_player_score(move, decrypt = False):
    return MOVE_VALUES[move][decrypt]

def part_one(moves) -> int:
    return sum([determine_player_score(move) for move in moves])


def part_two(moves) -> int:
    return sum([determine_player_score(move, decrypt=True) for move in moves])


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
