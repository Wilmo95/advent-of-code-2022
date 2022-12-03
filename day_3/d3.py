# part one
alphabet = "abcdefghijklmnopqrstuvwxyz"
lower_dict = {letter: idx for idx, letter in enumerate(alphabet, start=1)}
upper_dict = {letter: idx for idx, letter in enumerate(alphabet.upper(), start=27)}
my_dict = lower_dict | upper_dict

result = 0
with open("day_3\d3_data.txt", "r") as file:
    for line in file:
        l = len(line)
        string1 = line[: l // 2]
        string2 = line[len(string1) :]
        c = list(set(string1) & set(string2))[0]
        result += my_dict.get(c)

print(result)

# part two
with open("day_3\d3_data.txt", "r") as file:
    lines = file.readlines()

result = 0
for i in range(0, len(lines), 3):

    c = list(
        set(lines[i].rstrip()) & set(lines[i + 1].rstrip()) & set(lines[i + 2].rstrip())
    )[0]

    if c.isalpha():
        result += my_dict.get(c)

print(result)
