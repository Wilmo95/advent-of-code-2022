# Part One
with open("day_1\d1_data.txt", "r") as file:
    temp = 0
    max_calories = 0
    for line in file:
        if line == "\n":
            if temp > max_calories:
                max_calories = temp
            temp = 0
        else:
            temp += int(line)

    print(max_calories)

# Part Two
with open("day_1\d1_data.txt", "r") as file:
    elves = []
    temp = 0
    for line in file:
        if line == "\n" or "" or "":
            elves.append(temp)
            temp = 0
        else:
            temp += int(line)

    sorted_elves = sorted(elves)
    top_3 = sum(sorted_elves[-3:])
    print(sorted_elves[:])
    print(top_3)
