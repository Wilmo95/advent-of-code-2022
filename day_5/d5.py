import re

with open("day_5\d5_data.txt", "r") as file:
    lines = file.readlines()

stacks = [[], [], [], [], [], [], [], [], []]


for line in lines[:9]:
    parts = re.findall(r"(\[.\])|(    )", line)
    for i, p in enumerate(parts):
        if p[0] != "":
            stacks[i].insert(0, p[0][1])
print(stacks)

task = lines[10:]

### task one

for line in task:
    move = re.findall(r"[0-9]+", line)
    for i in range(int(move[0])):
        delete = stacks[int(move[1]) - 1].pop()
        stacks[int(move[2]) - 1].append(delete)


print(stacks)
result = ""
for s in stacks:
    result += result.join(s[-1])
print(result)

### task two
stacks = [[], [], [], [], [], [], [], [], []]


for line in lines[:9]:
    parts = re.findall(r"(\[.\])|(    )", line)
    for i, p in enumerate(parts):
        if p[0] != "":
            stacks[i].insert(0, p[0][1])
print(stacks)

result = ""
for line in task:
    move = re.findall(r"[0-9]+", line)
    delete = stacks[int(move[1]) - 1][-int(move[0]) :]
    stacks[int(move[1]) - 1] = stacks[int(move[1]) - 1][: -int(move[0])]
    stacks[int(move[2]) - 1].extend(delete)

for s in stacks:
    result += result.join(s[-1])
print(stacks)
print(result)
