import re


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def parse_input_file(file_input):
    return [part.split("\n") for part in file_input.split("\n\n")]


def parse_stack(input_stack):
    max_stack_value = int(max(input_stack[-1]))
    stack = [[] for _ in range(max_stack_value)]
    for row in input_stack[:-1]:
        for i, row_index in enumerate(range(1, len(row), 4)):
            if row[row_index].strip():
                stack[i].append(row[row_index])
    return stack

def parse_moves(input_moves):
    return [list(map(int, re.findall(r"[0-9]+", row))) for row in input_moves]

def execute_moves(stack, moves, is_over_9000):
    stack_mutate = [s[:] for s in stack]
    for num, start, end in moves:
        for i in range(num):
            crate = stack_mutate[start - 1].pop(0)
            stack_mutate[end - 1].insert(i if is_over_9000 else 0, crate)
    return "".join([s[0] for s in stack_mutate])

def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day5.txt")
    unparsed_stack, unparsed_moves = parse_input_file(file_input)
    stack = parse_stack(unparsed_stack)
    moves = parse_moves(unparsed_moves)
    part_one_value = execute_moves(stack, moves, False)
    part_two_value = execute_moves(stack, moves, True)
    print(part_one_value)
    print(part_two_value)


if __name__ == "__main__":
    main()
