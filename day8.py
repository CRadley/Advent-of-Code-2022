import math


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().splitlines()


def parse_file_input(file_input):
    trees = [tree for line in file_input for tree in map(int, line)]
    forest_width = len(file_input[0])
    return trees, forest_width

def is_edge_tree(i, trees, forest_width):
    return not i % forest_width or i % forest_width == forest_width - 1 or i < forest_width or i >= len(trees) - forest_width


def determine_los_trees(i, trees, forest_width):
    row = i // forest_width
    up = range(i -forest_width,0, -forest_width)
    down = range(i + forest_width, len(trees), forest_width)
    left = range(i - 1, row*forest_width-1,-1)
    right = range(i + 1, (row + 1)*forest_width)
    return up, down, left, right


def has_line_of_sight(i, trees, forest_width):
    return int(any([all(trees[i] > trees[j] for j in direction) for direction in determine_los_trees(i, trees, forest_width)]))

def is_tree_visible(i, trees, forest_width):
    return is_edge_tree(i, trees, forest_width) or has_line_of_sight(i, trees, forest_width)


def determine_visible_trees(trees, forest_width):
    return sum([is_tree_visible(i, trees, forest_width) for i, _ in enumerate(trees)])

def detemine_viewing_distance(tree_index, trees, direction):
    return next((i + 1 for i, neighbour_index in enumerate(direction) if trees[tree_index] <= trees[neighbour_index]), len(direction))


def determine_scenic_score(i, trees, forest_width):
    directions = determine_los_trees(i, trees, forest_width)
    return math.prod([detemine_viewing_distance(i, trees, direction) for direction in directions])


def detemine_best_scenic_score(trees, forest_width):
    return max([determine_scenic_score(i, trees, forest_width) for i, _ in enumerate(trees)])

def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day8.txt")
    trees, forest_width = parse_file_input(file_input)
    part_one_answer = determine_visible_trees(trees, forest_width)
    part_two_answer = detemine_best_scenic_score(trees, forest_width)
    print(part_one_answer)
    print(part_two_answer)

if __name__ == "__main__":
    main()

# 199272