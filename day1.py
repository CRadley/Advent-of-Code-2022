from functools import reduce
from typing import List

with open("resources/day1.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def elf_reducer(elves: List[int], line: str) -> List[int]:
    if line.isdigit():
        elves[-1] += int(line)
    else:
        elves.append(0)
    return elves

elves = reduce(elf_reducer, lines, [0])
print(max(elves))
print(sum(sorted(elves, reverse=True)[0:3]))