with open("input.txt", 'r') as f:
    input_text = f.readlines()

current_calories = 0

top_calories = [0] * 3

for c in input_text:
    this_calorie = c[:-1]
    if not this_calorie:
        if current_calories > top_calories[0]:
            top_calories.insert(0, current_calories)
        elif current_calories > top_calories[1]:
            top_calories.insert(1, current_calories)
        elif current_calories > top_calories[2]:
            top_calories.insert(2, current_calories)

        if len(top_calories) > 3:
            top_calories = top_calories[:3]
        current_calories = 0
    else:
        this_calorie = int(this_calorie)
        current_calories += this_calorie

print(f"Top calories: {top_calories}\nSum = {sum(top_calories)}")
