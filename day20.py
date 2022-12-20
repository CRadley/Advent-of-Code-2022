def read_input_file(file_path) -> str:
    with open(file_path, encoding="utf-8") as input_file:
        return input_file.read()


def parse_encryted_file(file_input):
    return list(map(lambda x: (x[0], int(x[1])), enumerate(file_input.splitlines())))


def wrap(offset, index, max_index):
    new_index = index + offset
    return new_index % max_index


def normalise(starting_index, max_index):
    return starting_index % max_index


def decrypt(encrypted, rounds=1, key=1):
    encrypted = [(e[0], e[1] * key) for e in encrypted]
    max_index = len(encrypted) - 1
    decrypted = encrypted[:]
    for _ in range(rounds):
        for e in encrypted:
            decrypted_index = decrypted.index(e)
            new_index = wrap(e[1], decrypted_index, max_index)
            decrypted.insert(new_index, decrypted.pop(decrypted_index))
    return decrypted


def determine_grove_coordinates(decrypted):
    zero = next(d for d in decrypted if not d[1])
    zero_index = decrypted.index(zero)
    unwrapped = zero_index + 1000, zero_index + 2000, zero_index + 3000
    wrapped = tuple([wrap(0, u, len(decrypted)) for u in unwrapped])
    coords = [decrypted[index][1] for index in wrapped]
    return sum(coords)


def main() -> None:
    """
    Main function
    """
    file_input = read_input_file("resources/day20.txt")
    encrypted = parse_encryted_file(file_input)
    decrypted = decrypt(encrypted)
    decrypted_with_key = decrypt(encrypted, 10, 811589153)
    part_one_value = determine_grove_coordinates(decrypted)
    print(part_one_value)
    part_two_value = determine_grove_coordinates(decrypted_with_key)
    print(part_two_value)


if __name__ == "__main__":
    main()


# 9945
