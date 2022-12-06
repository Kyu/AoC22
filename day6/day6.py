with open("input.txt", 'r') as f:
    input_text = f.read()

buffer4 = []
buffer14 = []

end4 = end14 = -1
rep4 = rep14 = -1

for i in range(len(input_text)):
    char = input_text[i]

    if end4 == -1:
        if len(buffer4) >= 4:
            if char not in buffer4 and not rep4:
                print(f"Buffer4: Position {i + 1}: {char} not in {buffer4}, and duplicates about to clear")
                end4 = i

            buffer4.pop(0)
            rep4 -= 1

        if char in buffer4:
            indices = [i for i, x in enumerate(buffer4) if x == char][-1]
            rep4 = max(rep4, indices)

        buffer4.append(char)

    if end14 == -1:
        if len(buffer14) >= 14:
            if char not in buffer14 and not rep14:
                print(f"Buffer14: Position {i + 1}: {char} not in {buffer14}, and duplicates about to clear")
                end14 = i

            buffer14.pop(0)
            rep14 -= 1

        if char in buffer14:
            indices = [i for i, x in enumerate(buffer14) if x == char][-1]
            rep14 = max(rep14, indices)

        buffer14.append(char)
