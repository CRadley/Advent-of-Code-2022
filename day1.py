from functools import reduce
from typing import List

with open("resources/day1.txt") as f:
    values = [line.strip() for line in f.readlines()]

def elf_reducer(current: List[int], value: str) -> List[int]:
    if value.isdigit():
        current[-1] += int(value)
    else:
        current.append(0)
    return current

elves = reduce(elf_reducer, values, [0])
print(max(elves))
print(sum(sorted(elves, reverse=True)[0:3]))