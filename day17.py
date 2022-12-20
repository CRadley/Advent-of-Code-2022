ROCKS = {
    0: ([2, 0], [3, 0], [4, 0], [5, 0]),
    1: ([3, 0], [2, 1], [3, 1], [4, 1], [3, 2]),
    2: ([2, 0], [3, 0], [4, 0], [4, 1], [4, 2]),
    3: ([2, 0], [2, 1], [2, 2], [2, 3]),
    4: ([2, 0], [3, 0], [2, 1], [3, 1]),
}

LEFT = "<"
RIGHT = ">"
DOWN = "D"


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_rocks(number):
    return [ROCKS[i % 5] for i in range(number)]


def current_max_height(fallen_rocks):
    if not fallen_rocks:
        return 0
    return max([pos[1] for fr in fallen_rocks for pos in fr]) + 1


def move_generator(moves):
    while True:
        for move in moves:
            yield move


def can_move_down(shape, rock_positions):
    if any(not s[1] for s in shape):
        return False
    for rp in rock_positions:
        for pos in rp:
            if any(s[1] - 1 == pos[1] for s in shape):
                return False
    return True


def add_jet(jet, rock, rocks):
    if jet == LEFT and all(r[0] - 1 >= 0 for r in rock):
        jet_left = [[r[0] - 1, r[1]] for r in rock]
        if all(r[0] >= 0 for r in jet_left) and not any(r in rp for rp in rocks for r in jet_left):
            return jet_left
    elif jet == RIGHT:
        jet_left = [[r[0] + 1, r[1]] for r in rock]
        if all(r[0] <= 6 for r in jet_left) and not any(r in rp for rp in rocks for r in jet_left):
            return jet_left
    return rock


def fall_down(rock, rock_positions):
    rock_copy = [r[:] for r in rock]
    for i in range(len(rock)):
        rock_copy[i][1] -= 1
    if any(r[1] == -1 for r in rock_copy):
        return rock
    elif any(r in rp for rp in rock_positions for r in rock_copy):
        return rock
    return rock_copy


def determine_max_height(moves, rocks):
    fallen_rocks = []
    jets = move_generator(moves)
    for rock in rocks:
        mh = current_max_height(fallen_rocks)
        rock_copy = [r[:] for r in rock]
        for i in range(len(rock_copy)):
            rock_copy[i][1] += mh + 3
        while True:
            jet = next(jets)
            jetted_rock = add_jet(jet, rock_copy, fallen_rocks)
            fallen_rock = fall_down(jetted_rock, fallen_rocks)
            if all(fr == jr for fr, jr in zip(jetted_rock, fallen_rock)):
                fallen_rocks.append(jetted_rock)
                break
            rock_copy = fallen_rock
        print(jetted_rock)
    return current_max_height(fallen_rocks)


def optimised_determine_max_height(moves, rock_num):
    height_rocks = {i: 1 for i in range(7)}
    fallen_rocks = []
    jets = move_generator(moves)
    for i in range(rock_num):
        rock = ROCKS[i % 5]
        # remember the highest rock at each position
        mh = max(v for v in height_rocks.values()) + 3
        print(rock, mh)


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day17.txt")
    rocks = determine_rocks(2022)
    max_height = determine_max_height(file_input, rocks)
    print(max_height)


if __name__ == "__main__":
    main()
