def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read().splitlines()

def determine_head_moves(move):
    direction, magnitude = move.split()
    magnitude = int(magnitude)
    if direction == "U":
        return [(0, 1) for _ in range(0, -magnitude, -1)]
    elif direction == "D":
        return [(0, -1) for _ in range(magnitude)]
    elif direction == "L":
        return [(-1, 0) for _ in range(0, -magnitude, -1)]
    elif direction == "R":
        return [(1, 0) for _ in range(magnitude)]

def determine_head_positions(file_input):
    current_head_position = [0, 0]
    head_positions = [[0, 0]]
    for line in file_input:
        moves = determine_head_moves(line)
        for move in moves:
            current_head_position[0] += move[0]
            current_head_position[1] += move[1]
            head_positions.append(current_head_position[:])
    return head_positions



def determine_unique_positions(head_moves, numknots):
    knot_positions = [[0, 0] for _ in range(numknots - 1)]
    tail_positions = [[0, 0]]
    for head_move in head_moves:
        for i, knot in enumerate(knot_positions):
            x_compare = head_move[0] if not i else knot_positions[i-1][0]
            y_compare = head_move[1] if not i else knot_positions[i-1][1]
            tail_x_diff = abs(knot[0] - x_compare)
            tail_y_diff = abs(knot[1] - y_compare)
            if 0 <= tail_x_diff <= 1 and 0 <= tail_y_diff <= 1:
                continue
            if tail_x_diff > 1 or (tail_x_diff == 1 and tail_y_diff > 1):
                knot[0] += 1 if knot[0] < x_compare else -1
            if tail_y_diff > 1 or (tail_y_diff == 1 and tail_x_diff > 1):
                knot[1] += 1 if knot[1] < y_compare else -1
            
            if knot not in tail_positions and i == len(knot_positions) - 1:
                tail_positions.append(knot[:])
    return len(tail_positions)

def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day9.txt")
    head_moves = determine_head_positions(file_input)
    part_one = determine_unique_positions(head_moves, 2)
    part_two = determine_unique_positions(head_moves, 10)
    print(part_one)
    print(part_two)
if __name__ == "__main__":
    main()