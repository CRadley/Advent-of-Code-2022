from string import ascii_letters


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().splitlines()


def determine_letter_value(letter) -> int:
    return ascii_letters.index(letter)


def determine_common_letter(letters) -> str:
    return set.intersection(*map(set, letters)).pop()


def part_one(bags) -> int:
    return sum(determine_letter_value(determine_common_letter([bag[:len(bag)//2], bag[len(bag)//2:]])) for bag in bags)


def part_two(bags) -> int:
    groups = [bags[index:index+3] for index in range(0, len(bags), 3)]
    return sum(determine_letter_value(determine_common_letter(group)) for group in groups)


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day3.txt")
    part_one_value = part_one(file_input)
    part_two_value = part_two(file_input)
    print(part_one_value)
    print(part_two_value)


if __name__ == "__main__":
    main()
