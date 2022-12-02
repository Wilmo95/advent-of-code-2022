### Part one

# A for Rock
# B for Paper
# C for Scissors
# X for Rock
# Y for Paper
# Z for Scissors
# 1 rock
# 2 paper
# 3 scissors

results = {
    "A Y": 8,
    "A X": 4,
    "A Z": 3,
    "B Y": 5,
    "B X": 1,
    "B Z": 9,
    "C Y": 2,
    "C X": 7,
    "C Z": 6,
}

with open("day_2\d2_data.txt", "r") as file:
    result = 0
    for line in file:
        result += results[line.rstrip()]
    print(result)

# Part two

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
results = {
    "A Y": 4,
    "A X": 3,
    "A Z": 8,
    "B Y": 5,
    "B X": 1,
    "B Z": 9,
    "C Y": 6,
    "C X": 2,
    "C Z": 7,
}

with open("day_2\d2_data.txt", "r") as file:
    result2 = 0
    for line in file:
        result2 += results[line.rstrip()]
    print(result2)
