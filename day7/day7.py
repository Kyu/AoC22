from enum import Enum

with open("input.txt", 'r') as f:
    input_text = f.readlines()

class BrowsingMode(Enum):
    IDLE = 0
    LISTING = 1

class File:
    def __init__(self, name, size=0, is_directory=False, parent=None):
        self.name = name
        self.size = size
        self.is_directory = is_directory
        self.parent = parent
        if self.is_directory:
            self.children = {}
        else:
            self.children = None

    def add_child(self, file):
        if not self.is_directory:
            return
        file.parent = self
        self.children[file.name] = file

        # self.parent.size += file.size
        # self.size += file.size

    def get_child(self, name):
        if not self.is_directory:
            return
        return self.children.get(name)

main_dir = File('/', is_directory=True)
main_dir.parent = main_dir

current_dir = main_dir
current_mode = BrowsingMode.IDLE

for i in input_text:
    if i.startswith("$"):
        current_mode = BrowsingMode.IDLE

    if current_mode == BrowsingMode.IDLE:
        command = i[1:].split()
        if command[0] == "cd":
            to_go = command[1]
            if to_go == '/':
                current_dir = main_dir
            elif to_go == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_child(to_go)
        elif command[0] == "ls":
            current_mode = BrowsingMode.LISTING
    elif current_mode == BrowsingMode.LISTING:
        file_data = i.split()

        if file_data[0] != "dir":
            f_size = int(file_data[0])

            main_dir.size += f_size

            f_name = file_data[1]
            current_dir.add_child(File(f_name, f_size))
        else:
            current_dir.add_child(File(file_data[1], is_directory=True))


def print_children(fr: File, depth=0):
    tab = '\t'
    if fr.is_directory:
        for x in fr.children.values():
            if x.is_directory:
                print(f"{tab*depth}{x.name}: - {x.size}")
                print_children(x, depth + 1)
            else:
                print(f"{tab*depth}{x.name}: {x.size}")

# print_children(main_dir)

disk_used = main_dir.size
threshold_count = 0
smallest_dir = disk_used

space_needed = 70000000 - 30000000 - disk_used


def count_sizes(fr: File):
    global threshold_count, smallest_dir

    total = fr.size
    if fr.is_directory:
        for x in fr.children.values():
            total += count_sizes(x)

    if fr.is_directory:
        if total <= 100000:
            threshold_count += total
        if total + space_needed > 0:
            smallest_dir = min(smallest_dir, total)

    return total

count_sizes(main_dir)

print(f"Total: {disk_used}")
print(f"Threshold count: {threshold_count}")
print(f"Smallest directory: {smallest_dir}")

