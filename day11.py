from dataclasses import dataclass
from functools import reduce
from typing import List


OPERATIONS = {
    "+": lambda x, y: x + y if y else x + x,
    "*": lambda x, y: x * y if y else x * x,
}


@dataclass
class Monkey:
    items: List[int]
    operation: str
    operation_value: int
    test_value: int
    true_monkey: int
    false_monkey: int
    item_inspections: int = 0


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_monkeys(file_input):
    monkeys = []
    for lines in file_input.split("\n\n"):
        details = lines.split("\n")
        starting_items = list(map(int, details[1].split(": ")[1].split(",")))
        operator = "+" if "+" in details[2] else "*"
        operation_value = 0 if details[2].split(
            " ")[-1] == "old" else int(details[2].split(" ")[-1])
        test_value = int(details[3].split(" ")[-1])
        true_monkey = int(details[4].split(" ")[-1])
        false_monkey = int(details[5].split(" ")[-1])
        monkeys.append(Monkey(starting_items, operator,
                              operation_value, test_value, true_monkey, false_monkey))
    return monkeys


def determine_monkey_business(monkeys, rounds, divide_by_3):
    modulo = reduce(lambda x, y: x * y, [m.test_value for m in monkeys], 1)
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items[:]:
                monkey.item_inspections += 1
                new_item_value = OPERATIONS[monkey.operation](
                    item, monkey.operation_value) % modulo
                if divide_by_3:
                    new_item_value //= 3
                if not new_item_value % monkey.test_value:
                    monkeys[monkey.true_monkey].items.append(new_item_value)
                else:
                    monkeys[monkey.false_monkey].items.append(new_item_value)
                monkey.items.pop(0)
    inspections = [m.item_inspections for m in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day11.txt")
    monkeys = determine_monkeys(file_input)
    part_one_value = determine_monkey_business(monkeys, 20, True)
    monkeys = determine_monkeys(file_input)
    part_two_value = determine_monkey_business(monkeys, 10000, False)
    print(part_one_value)
    print(part_two_value)


if __name__ == "__main__":
    main()


# 14426171625
