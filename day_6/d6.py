with open("day_6\d6_data.txt", "r") as file:
    lines = file.readlines()[0]

l = len(lines)
for i in range(0, l):
    s = set(lines[i : i + 4])
    if len(s) == 4:
        print(i + 4)
        break

for i in range(0, l):
    s = set(lines[i : i + 14])
    if len(s) == 14:
        print(i + 14)
        break
