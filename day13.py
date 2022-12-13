from math import prod
from re import match

def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def determine_packets(file_input):
    return [(eval(line.split("\n")[0]), eval(line.split("\n")[1])) for line in file_input.split("\n\n")]

def determine_packets_two(file_input):
    file_input += "\n[[2]]\n[[6]]"
    return [eval(line) for line in file_input.splitlines() if line]

def is_correct_order(left_packet, right_packet):
    if isinstance(left_packet, int) and isinstance(right_packet, int):
        if left_packet < right_packet:
            return True
        elif right_packet < left_packet:
            return False
        return None
    elif isinstance(left_packet, list) and isinstance(right_packet, list):
        for l, r in zip(left_packet, right_packet):
            correct = is_correct_order(l, r)
            if correct is None:
                continue
            return correct
        return None if len(left_packet) == len(right_packet) else len(left_packet) < len(right_packet)
    elif isinstance(left_packet, list) and isinstance(right_packet, int):
        return is_correct_order(left_packet,[right_packet])
    else:
        return is_correct_order([left_packet], right_packet)
        
def part_one(packets):
    total = 0
    for i, packet in enumerate(packets):
        valid = is_correct_order(*packet)
        if valid:
            total += i + 1
    return total

def determine_decoder_key(packets):
    for i in range(len(packets)):
        for j in range(len(packets)):
            if j != i and is_correct_order(packets[i], packets[j]):
                packets[i], packets[j] = packets[j], packets[i]
    decoder_key_indexes = []
    for i, packet in enumerate(packets, 1):
        if match(r"^\[\[(2|6)\]\]$",str(packet)):
            decoder_key_indexes.append(i)
    return prod(decoder_key_indexes)


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day13.txt")
    packets = determine_packets(file_input)
    part_one_value = part_one(packets)
    print(part_one_value)

    part_two_packets = determine_packets_two(file_input)
    part_two_value = determine_decoder_key(part_two_packets)
    print(part_two_value)
if __name__ == "__main__":
    main()