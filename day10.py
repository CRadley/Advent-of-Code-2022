def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().splitlines()


def determine_command(line):
    split_line = line.split(" ")
    if len(split_line) == 1:
        return tuple(split_line)
    return split_line[0], int(split_line[1])


def determine_commands(file_input):
    return (determine_command(line) for line in file_input)


def part_one(commands, max_cycles) -> int:
    IMPORTANT_CYCLES = (20, 60, 100, 140, 180, 220)
    important_cycles_values = []
    x = 1
    mid_addx_cycle = False
    pixels = ["."] * 240
    for i in range(1, max_cycles + 1):
        current_sprite_pixels = list(
            filter(lambda y: 0 <= y < 40, [x - 1, x, x + 1]))
        current_row = i // 40
        for sp in current_sprite_pixels:
            if i - (current_row * 40) - 1 == sp:
                pixels[i - 1] = "#"
        if i in IMPORTANT_CYCLES:
            important_cycles_values.append(x * i)
        if not mid_addx_cycle:
            command = next(commands, ())
        if len(command) == 2:
            if mid_addx_cycle:
                mid_addx_cycle = False
                x += command[1]
            else:
                mid_addx_cycle = True
    return sum(important_cycles_values), pixels


def display_pixels(pixels):
    for i in range(0, 240, 40):
        print("".join(pixels[i:i+40]))


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day10.txt")
    commands = determine_commands(file_input)
    cycle_values, pixels = part_one(commands, 240)
    print(cycle_values)
    display_pixels(pixels)


if __name__ == "__main__":
    main()
