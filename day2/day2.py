with open("input.txt", 'r') as f:
    input_text = f.readlines()


def part1():
    point_allocator = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    my_points = 0

    for i in input_text:
        split = i.strip().split()
        chr1 = split[0]
        chr2 = split[1]

        opponent = point_allocator.get(chr1)
        me = point_allocator.get(chr2)

        these_points = me

        if me == opponent:
            these_points += 3
        elif me == (opponent % 3) + 1:
            these_points += 6

        my_points += these_points

    print(f"Part 1: {my_points}")


def part2():
    point_allocator = {"@": 3, "A": 1, "B": 2, "C": 3, "D": 1, "X": 0, "Y": 3, "Z": 6}

    my_points = 0
    for i in input_text:
        split = i.strip().split()
        chr1 = split[0]
        chr2 = split[1]

        opponent = point_allocator.get(chr1)
        result = point_allocator.get(chr2)

        these_points = result

        if result == 3:
            these_points += opponent
        elif result == 6:
            played = chr(ord(chr1) + 1)
            these_points += point_allocator.get(played)
        elif result == 0:
            played = chr(ord(chr1) - 1)
            these_points += point_allocator.get(played)

        my_points += these_points

    print(f"Part 2: {my_points}")


if __name__ == "__main__":
    part1()
    part2()
