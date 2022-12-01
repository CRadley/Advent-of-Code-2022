from functools import reduce
from typing import List

with open("resources/day1.txt") as f:
    values = [line.strip() for line in f.readlines()]

def elf_reducer(elves: List[int], value: str) -> List[int]:
    if value.isdigit():
        elves[-1] += int(value)
    else:
        elves.append(0)
    return elves

elves = reduce(elf_reducer, values, [0])
print(max(elves))
print(sum(sorted(elves, reverse=True)[0:3]))