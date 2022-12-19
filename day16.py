from typing import List
from dataclasses import dataclass
from re import compile, match

VALVE_PATTERN = compile(
    r"Valve ([A-Z]{2}) has flow rate=([\d]+); tunnel(s)? lead(s)? to valve(s)? ([A-Z, ]+)")


@dataclass
class Valve:
    name: str
    flow_rate: int
    tunnels: List[str]


def read_input_file(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_valves(file_input):
    valves = []
    for line in file_input.splitlines():
        groups = match(VALVE_PATTERN, line).groups()
        valve = Valve(groups[0], int(groups[1]), list(
            map(str.strip, groups[5].split(","))))
        valves.append(valve)
    return valves


def part_one(valves):
    paths = []

    print(valves)


def main() -> None:
    file_input = read_input_file("resources/day16.txt")
    valves = determine_valves(file_input)
    part_one_value = part_one(valves)


if __name__ == "__main__":
    main()
