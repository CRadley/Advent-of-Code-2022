"""
Advent of Code: Day 1
"""
from typing import List


def read_input_file(file_path: str) -> str:
    """
    Reads and returns input file content
    """
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_elves(file_input: str) -> List[int]:
    """
    Determines the calorie count for each elf
    """
    return [sum(map(int, elf.split())) for elf in file_input.split("\n\n")]


def determine_largest_calories(elves: List[int]) -> int:
    """
    Returns the largest calorie value
    """
    return max(elves)


def determine_largest_calorie_sum(elves: List[int]) -> int:
    """
    Determines the sum of the three largest calorie values
    """
    return sum(sorted(elves, reverse=True)[0:3])


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day1.txt")
    elves = determine_elves(file_input)
    print(determine_largest_calories(elves))
    print(determine_largest_calorie_sum(elves))


if __name__ == "__main__":
    main()
