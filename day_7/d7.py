from collections import defaultdict

total = 0
max_size = 100000
sizes = defaultdict(int)

with open("day_7\d7_data.txt", "r") as file:
    data = file.readlines()
data = [line.strip() for line in data]

file_path = []

for line in data:
    if line.startswith("$ cd"):
        directory = line.split()[-1]

        if directory == "..":
            file_path.pop()

        else:
            file_path.append(directory)
    elif line.startswith("$ ls"):
        continue

    else:
        size, name = line.split()
        if size.isdigit():
            size = int(size)
            for i in range(len(file_path)):
                sizes["/".join(file_path[: i + 1])] += size
for key, value in sizes.items():
    if value <= 100_000:
        total += value

print(total)

main = sizes["/"]
print(main)
space = 70000000 - main
needed_space = 30000000 - space
print(needed_space)

minimum = 99999999
for k, v in sizes.items():
    if space + v >= 30000000 and minimum > v:
        minimum = v
print(minimum)
