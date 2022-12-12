from string import ascii_lowercase
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Any


def determine_ascii_index(ascii_value):
    if ascii_value == "S":
        return 0
    if ascii_value == "E":
        return 25
    return ascii_lowercase.index(ascii_value)

@dataclass
class Node:
    index: int
    prev: Any
    steps: int = 0

    def determine_neighbours(self, height_map, resolution):
        ascii_index = determine_ascii_index(height_map[self.index])
        neighbours = []
        if self.index % resolution and determine_ascii_index(height_map[self.index - 1]) <= ascii_index + 1:
            neighbours.append(Node(self.index - 1, self, self.steps))
        if self.index % resolution < resolution - 1 and determine_ascii_index(height_map[self.index + 1]) <= ascii_index + 1:
            neighbours.append(Node(self.index + 1, self, self.steps))
        if self.index > resolution and determine_ascii_index(height_map[self.index - resolution]) <= ascii_index + 1:
            neighbours.append(Node(self.index - resolution, self, self.steps))
        if self.index < len(height_map) - resolution and determine_ascii_index(height_map[self.index + resolution]) <= ascii_index + 1:
            neighbours.append(Node(self.index + resolution, self, self.steps))
        return neighbours

    def __eq__(self, node):
        return self.index == node.index
    
    def __lt__(self, other):
        return self.steps < other.steps
    
def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().splitlines()


def determine_height_map(file_input):
    return [c for line in file_input for c in line], len(file_input[0])


def find_starting_index(height_map):
    return height_map.index("S")


def find_starting_indexes(height_map, starting_characters):
    return [i for i, value in enumerate(height_map) if value in starting_characters]


def find_end_index(height_map):
    return height_map.index("E")

def determine_path_length(node):
    path = []
    while node.prev:
        path.append(node.index)
        node = node.prev
    return len(path)


def determine_fewest_steps(height_map, resolution, starting_characters):
    starting_indexes = find_starting_indexes(height_map, starting_characters)
    path_lengths = []
    ending_index = find_end_index(height_map)
    for starting_index in starting_indexes:
        start_node = Node(starting_index, None)
        end_node = Node(ending_index, None)
        open_nodes = []
        closed_nodes = {}
        heappush(open_nodes, start_node)
        while open_nodes:
            current_node = heappop(open_nodes)
            closed_nodes[current_node.index] = None
            if current_node == end_node:
                path_lengths.append(determine_path_length(current_node))
                break
            for node in current_node.determine_neighbours(height_map, resolution):
                if node.index in closed_nodes:
                    continue
                node.steps += 1
                if node in open_nodes:
                    continue
                heappush(open_nodes, node)
    return min(path_lengths)
def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day12.txt")
    height_map, resolution = determine_height_map(file_input)
    part_one_answer = determine_fewest_steps(height_map, resolution, ["S"])
    print(part_one_answer)
    part_two_answer = determine_fewest_steps(height_map, resolution, ["S", "a"])
    print(part_two_answer)


if __name__ == "__main__":
    main()

# P1 472