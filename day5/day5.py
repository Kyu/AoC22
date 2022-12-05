from string import ascii_uppercase


with open("input.txt", 'r') as f:
    input_text = f.readlines()


crates = dict()

def get_crate_data(line: str):
    for i in range(len(line)):
        if i  % 4 == 1:
            item = line[i]
            if item in ascii_uppercase:
                crate_number = (i // 4) + 1

                this_crate = crates.get(crate_number, [])

                this_crate.insert(0, item)
                crates[crate_number] = this_crate


for start in input_text:
    if '[' in start:
        get_crate_data(start)
    else:
        break


def create_crate_string(cr: dict):
    crate_string = ""
    for k,v in sorted(cr.items()):
        print(f"{k}: {v[-1]}")
        crate_string += v[-1]

    return crate_string


def get_command_data(command: str):
    cmd = command.split('from')
    number, directions = int(cmd[0]), cmd[1].split('to')
    origin, destination = int(directions[0]), int(directions[1])

    return number, origin, destination


def part1():
    p1_crates = crates.copy()

    for text in input_text:
        if 'move' in text:
            command = text[5:]

            number, origin, destination = get_command_data(command)

            while number:
                number -= 1

                obj = p1_crates.get(origin, []).pop()
                p1_crates.get(destination, []).append(obj)

    return p1_crates



def part2():
    p2_crates = crates.copy()

    for text in input_text:
        if 'move' in text:
            command = text[5:]
            number, origin, destination = get_command_data(command)

            objects = p2_crates.get(origin, [])

            to_move = objects[-number:]
            p2_crates[origin] = objects[:-number]

            p2_crates.get(destination, []).extend(to_move)

    return p2_crates

if __name__ == "__main__":
    print(f"Part 1: {create_crate_string(part1())}")
    print(f"Part 2: {create_crate_string(part2())}")
