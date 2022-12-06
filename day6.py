def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().strip()


def determine_unique_pointer(file_input, offset):
    return next((i + offset for i in range(len(file_input)) if len(set(file_input[i:i+offset])) == offset), None)


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day6.txt")
    part_one_value = determine_unique_pointer(file_input, 4)
    part_two_value = determine_unique_pointer(file_input, 14)
    print(part_one_value)
    print(part_two_value)


if __name__ == "__main__":
    main()
