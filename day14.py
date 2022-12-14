import re


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_positions(x, y, x1, y1):
    if x == x1:
        modifier = 1 if y < y1 else -1
        y_positions = range(y, y1 + modifier, modifier)
        return list(zip([x] * len(y_positions), y_positions))
    modifier = 1 if x < x1 else -1
    x_positions = range(x, x1 + modifier, modifier)
    return list(zip(x_positions, [y] * len(x_positions)))


def convert_rock_position(rock):
    return list(map(int, rock.split(",")))


def determine_sub_invalid_rocks(rock_positions):
    rocks = []
    for i in range(1, (len(rock_positions)//2 + 1)):
        new_positions = [(r[0], r[1] + i + 1) for r in rock_positions[i:-i]]
        rocks.extend(new_positions)
    return rocks


def determine_rocks(file_input):
    valid_rocks = []
    for line in file_input.splitlines():
        matches = list(map(convert_rock_position,
                           re.findall(r"[\d]+,[\d]+", line)))
        for i, rock in enumerate(matches, 1):
            if i == len(matches):
                continue
            next_rock = matches[i]
            positions = determine_positions(*rock, *next_rock)
            valid_rocks.extend(positions)
    return list(map(list, set(valid_rocks)))


def determine_max_y_value(rock_positions):
    return max(map(lambda x: x[1], rock_positions))


def pos_to_string(pos):
    return f"{pos[0]}:{pos[1]}"


def detemine_next_positions(pos):
    down = [pos[0], pos[1] + 1]
    down_left = [pos[0] - 1, pos[1] + 1]
    down_right = [pos[0] + 1, pos[1] + 1]
    return down, down_left, down_right


def is_valid_move(pos, sand, rocks):
    return pos_to_string(pos) not in sand and pos_to_string(pos) not in rocks


def determine_sand_units(rock_positions, is_infinite):
    max_rock_y = determine_max_y_value(rock_positions)
    if is_infinite:
        max_rock_y += 2
        rock_positions.extend([[i, max_rock_y] for i in range(1000)])  # Lol
    rocks = {pos_to_string(pos): 0 for pos in rock_positions}
    sand_positions = {}
    current_sand_position = [500, 0]
    while True:
        if pos_to_string([500, 0]) in sand_positions or (not is_infinite and current_sand_position[1] == max_rock_y):
            return len(sand_positions)
        down, left, right = detemine_next_positions(current_sand_position)
        next_position = next(
            (pos for pos in (down, left, right) if is_valid_move(pos, sand_positions, rocks)), None)
        if next_position:
            current_sand_position = next_position
            continue
        sand_positions[pos_to_string(current_sand_position)] = 0
        current_sand_position = [500, 0]


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day14.txt")
    rocks = determine_rocks(file_input)

    sand_units = determine_sand_units(rocks, False)
    print(sand_units)
    part_two = determine_sand_units(rocks, True)
    print(part_two)


if __name__ == "__main__":
    main()
