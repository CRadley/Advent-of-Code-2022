def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().splitlines()


def parse_file_input(file_input):
    return [line.split() for line in file_input]


def determine_directory_structure(commands):
    dirs = {}
    path = []
    for command in commands:
        if command[0] == "$" and command[1] == "cd":
            if command[2] == "..":
                path.pop()
            else:
                path.append(command[2])
            if "".join(path) not in dirs:
                dirs["".join(path)] = 0
        elif command[1] != "ls" and command[0] != "dir":
            unique_paths = ["".join(path[:i + 1]) for i in range(len(path))]
            for up in unique_paths:
                dirs[up] += int(command[0])
    return dirs


def part_one(dirs):
    return sum(value for value in dirs.values() if value <= 100000)


def part_two(dirs):
    current_available = 70000000 - dirs["/"]
    return min([value for value in dirs.values() if current_available + value >= 30000000])

def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day7.txt")
    commands = parse_file_input(file_input)
    dirs = determine_directory_structure(commands)
    part_one_value = part_one(dirs)
    part_two_value = part_two(dirs)
    print(part_one_value)
    print(part_two_value)


if __name__ == "__main__":
    main()
