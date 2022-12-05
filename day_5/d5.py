with open("day_5\d5_data.txt", "r") as file:
    lines = file.readlines()

stacks = [[], [], [], [], [], [], [], [], [], []]
# regex tu bedzie
for i in lines[:9]:
    for x in i:
        # print(x)
        print(x.split(" "))
