with open("input.txt", 'r') as f:
    input_text = f.readlines()

num_incl = 0
num_overlap = 0


for i in input_text:
    split = i.split(",")

    part1 = split[0].split("-")
    part2 = split[1].split("-")

    p1_start, p1_stop = int(part1[0]),int(part1[1])
    p2_start, p2_stop = int(part2[0]), int(part2[1])

    if (p1_start <= p2_start and p1_stop >= p2_stop) or (p2_start <= p1_start and p2_stop >= p1_stop):
        num_incl += 1
    if (p1_start <= p2_start <= p1_stop) or (p2_start <= p1_start <= p2_stop):
        num_overlap += 1

print(f"Number Inclusive: {num_incl}\nNumber Overlap: {num_overlap}")