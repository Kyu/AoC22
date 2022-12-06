from string import ascii_uppercase
import time

import copy


with open("aoc_2022_day05_large_input_GoT_6mb.txt   ", 'r') as f:
    input_text = f.readlines()


crates = {}

def get_crate_data(line: str):
    for i in range(len(line)):
        if i  % 4 == 1:
            item = line[i]
            if item in ascii_uppercase:
                crate_number = (i // 4) + 1

                this_crate = crates.get(crate_number, [])

                this_crate.append(item)
                crates[crate_number] = this_crate


print("Starting crate parsing")
now = time.time()
for start in input_text:
    if '[' in start:
        get_crate_data(start)
    else:
        break

for crt in crates.values():
    crt.reverse()

print(f"Done! Took {time.time() - now}")
def create_crate_string(cr: dict):
    crate_string = ''
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
    p1_crates = copy.deepcopy(crates)

    for text in input_text:
        if 'move' in text:
            command = text[5:]
            number, origin, destination = get_command_data(command)

            objects_1 = p1_crates[origin]

            to_move_1 = objects_1[-number:]
            to_move_1.reverse()

            del p1_crates[origin][-number:]
            p1_crates[destination].extend(to_move_1)

    return p1_crates

def part2():
    p2_crates = copy.deepcopy(crates)

    for text in input_text:
        if 'move' in text:
            command = text[5:]
            number, origin, destination = get_command_data(command)

            objects_2 = p2_crates[origin]

            to_move_2 = objects_2[-number:]
            del p2_crates[origin][-number:]
            p2_crates[destination].extend(to_move_2)

    return p2_crates

if __name__ == "__main__":
    print("Starting: ")

    now = time.time()
    print(f"Part 1: {create_crate_string(part1())}")
    print(f"Done! Took {time.time() - now}")

    now = time.time()
    print(f"Part 2: {create_crate_string(part2())}")
    print(f"Done! Took {time.time() - now}")
