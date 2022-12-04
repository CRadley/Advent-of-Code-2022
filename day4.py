import re


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().splitlines()


def determine_pairs(file_input) -> int:
    return [list(map(int, re.split(r"[-,]", line))) for line in file_input]


def detemine_contained_pair(a, b, c, d):
    return (c <= a <= d and c <= b) <= d or (a <= c <= b and a <= d <= b)


def detemine_overlapped_pair(a, b, c, d):
    return c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b


def part_one(pairs) -> int:
    return sum([detemine_contained_pair(*pair) for pair in pairs])


def part_two(pairs) -> int:
    return sum([detemine_overlapped_pair(*pair) for pair in pairs])


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day4.txt")
    pairs = determine_pairs(file_input)
    part_one_value = part_one(pairs)
    part_two_value = part_two(pairs)
    print(part_one_value)
    print(part_two_value)


if __name__ == "__main__":
    main()
