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
    for i in range(1,(len(rock_positions)//2 + 1)):
        new_positions = [(r[0], r[1] + i + 1) for r in rock_positions[i:-i]]
        rocks.extend(new_positions)
    return rocks

def determine_rocks_and_air(file_input):
    valid_rocks = []
    air = []
    for line in file_input.splitlines():
        matches = list(map(convert_rock_position,re.findall(r"[\d]+,[\d]+", line)))
        for i, rock in enumerate(matches, 1):
            if i == len(matches):
                continue
            next_rock = matches[i]
            positions = determine_positions(*rock, *next_rock)
            if rock[1] == next_rock[1]:
                air.extend(determine_sub_invalid_rocks(positions))
                valid_rocks.extend(positions)
            else:
                valid_rocks.extend(positions)
    max_rock_y = determine_max_y_value(valid_rocks)
    air = list(filter(lambda x: x not in valid_rocks and x[1] <= max_rock_y + 2, air))
    return list(map(list, set(valid_rocks))), list(map(list, set(air)))

def determine_max_y_value(rock_positions):
    return max(map(lambda x: x[1], rock_positions))

def reset_sand_position():
    return [500, 0]


def determine_sand_units(rock_positions):
    max_rock_y = determine_max_y_value(rock_positions)
    sand_positions = []
    current_sand_position = reset_sand_position()
    while True:
        if current_sand_position[1] >= max_rock_y:
            return len(sand_positions)
        down = [current_sand_position[0], current_sand_position[1] + 1]
        down_left = [current_sand_position[0] - 1, current_sand_position[1] + 1]
        down_right = [current_sand_position[0] + 1, current_sand_position[1] + 1]

        if down not in sand_positions and down not in rock_positions:
            current_sand_position = down
            continue
        elif down_left not in sand_positions and down_left not in rock_positions:
            current_sand_position = down_left
            continue
        elif down_right not in sand_positions and down_right not in rock_positions:
            current_sand_position = down_right
            continue
        sand_positions.append(current_sand_position)
        current_sand_position = reset_sand_position()

def determine_max_sand(n):
    return 2 * (n * (n-1)//2) + n

def determine_max_sand_units(valid_rocks, air):
    max_rock_y = determine_max_y_value(valid_rocks) + 2
    max_sand = determine_max_sand(max_rock_y)
    return max_sand - len(valid_rocks) - len(air)


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day14.txt")
    rocks, air = determine_rocks_and_air(file_input)

    sand_units = determine_sand_units(rocks)
    print(sand_units)

    part_two = determine_max_sand_units(rocks, air)
    print(part_two)
if __name__ == "__main__":
    main()


# 23900 too high