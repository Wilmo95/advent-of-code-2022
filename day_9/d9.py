head = [0, 0]
tail = [0, 0]
visited = list()


def move_head(direction):
    match direction:
        case "U":
            head[1] += 1
        case "D":
            head[1] -= 1
        case "L":
            head[0] -= 1
        case "R":
            head[0] += 1


def move_tail():
    diff_y = head[1] - tail[1]
    diff_x = head[0] - tail[0]
    if abs(diff_x) <= 1 and abs(diff_y) <= 1:
        if tail not in visited:
            visited.append([tail[0], tail[1]])
    else:
        if diff_y == 2 and diff_x == 0:  # up
            tail[1] += 1

        elif diff_y == -2 and diff_x == 0:  # down
            tail[1] -= 1

        elif diff_y == 0 and diff_x == 2:  # right
            tail[0] += 1

        elif diff_y == 0 and diff_x == -2:  # left
            tail[0] -= 1

        elif (diff_y == 2 and diff_x == 1) or (
            diff_y == 1 and diff_x == 2
        ):  # up right corner
            tail[0] += 1
            tail[1] += 1

        elif (diff_y == -2 and diff_x == 1) or (
            diff_y == -1 and diff_x == 2
        ):  # down right corner
            tail[0] += 1
            tail[1] -= 1

        elif (diff_y == 2 and diff_x == -1) or (
            diff_y == 1 and diff_x == -2
        ):  # up left corner
            tail[0] -= 1
            tail[1] += 1

        elif (diff_y == -2 and diff_x == -1) or (
            diff_y == -1 and diff_x == -2
        ):  # down left corner
            tail[0] -= 1
            tail[1] -= 1

        if tail not in visited:
            visited.append([tail[0], tail[1]])


with open("day_9\d9_data.txt", "r") as file:
    data = file.readlines()
data = [line.strip().split(" ") for line in data]

for move in data:
    for i in range(int(move[1])):
        move_head(move[0])
        move_tail()


print(len(visited))
