import string

with open("input.txt", 'r') as f:
    input_text = f.readlines()

priority_map = {i: ord(i) - 96 for i in string.ascii_lowercase}
priority_map.update({i: ord(i) - 38 for i in string.ascii_uppercase})

sum_priorities = 0

group_stuff = set()
group_priorities = 0

for el in range(len(input_text)):
    i = input_text[el][:-1]

    if not group_stuff:
        group_stuff = set(i)
    else:
        group_stuff = set(i).intersection(group_stuff)

    if el % 3 == 2:
        for g_id in group_stuff:
            group_priorities += priority_map.get(g_id, 0)
            break
        group_stuff = set()

    split = len(i) // 2

    first = i[:split]
    second = i[split:]

    set1 = set(first)
    set2 = set(second)

    common = set1.intersection(set2)
    dupe = ''

    for item in common:
        dupe = item
        break

    priority = priority_map.get(dupe, 0)
    sum_priorities += priority

print(f"Sum Priorities = {sum_priorities}\nGroup Priorities = {group_priorities}")
