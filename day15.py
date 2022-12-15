import re
from collections import Counter, defaultdict


def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_positions(file_input):
    return [list(map(int, re.findall(r"([-0-9]+)", line))) for line in file_input.splitlines()]


def manhatten_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def determine_invalid_points(min_x, max_x, md, sx, sy, target_y):
    points = {}
    for x in range(min_x, max_x + 1):
        if md >= manhatten_distance(sx, sy, x, target_y):
            points[(x, target_y)] = 0
    return points


def part_one(positions, debug):
    invalid_points = []
    for sx, sy, bx, by in positions:
        md = manhatten_distance(sx, sy, bx, by)
        max_x = sx + md
        min_x = sx - md
        potential_points = determine_invalid_points(
            min_x, max_x, md, sx, sy, debug)
        invalid_points.extend(list(filter(lambda point: point != (
            sx, sy) and point != (bx, by), potential_points)))
    invalid_points = list(set(invalid_points))
    points = [ip for ip in invalid_points if ip[1] == debug]
    return len(points)


def determine_lines(min_x, max_x, min_y, max_y, sx, sy, offset):
    return [
        [(min_x-offset, sy), (sx, min_y-offset)],
        [(min_x-offset, sy), (sx, max_y+offset)],
        [(max_x+offset, sy), (sx, min_y-offset)],
        [(max_x+offset, sy), (sx, max_y+offset)],
    ]


def find_intersection(line_1, line_2):
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    x1, y1, x2, y2 = *line_1[0], *line_1[1]
    x3, y3, x4, y4 = *line_2[0], *line_2[1]
    divisor = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if not divisor:
        return None
    px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)) // divisor
    py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)) // divisor
    return (px, py)


def is_within_bounds(pos):
    return 0 <= pos[0] <= 4000000 and 0 <= pos[1] <= 4000000


def part_two(positions):
    lines = []
    for sx, sy, bx, by in positions:
        md = manhatten_distance(sx, sy, bx, by)
        max_x = sx + md
        min_x = sx - md
        max_y = sy + md
        min_y = sy - md
        lines.extend(determine_lines(min_x, max_x, min_y, max_y, sx, sy, 1))
    intersections = []
    for line in lines:
        for other in lines:
            if line == other:
                continue
            i = find_intersection(line, other)
            if i:
                intersections.append(i)
    intersections = filter(is_within_bounds, intersections)
    for i in set(intersections):
        if all(manhatten_distance(sx, sy, bx, by) < manhatten_distance(sx, sy, i[0], i[1]) for sx, sy, bx, by in positions):
            return i[0] * 4000000 + i[1]


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day15.txt")
    positions = determine_positions(file_input)
    # part_one_value = part_one(positions, 10)
    # print(part_one_value)
    part_two_value = part_two(positions)
    print(part_two_value)


if __name__ == "__main__":
    main()
