import numpy as np

with open("day_8\d8_data.txt", "r") as file:
    data = file.readlines()
data = [line.strip() for line in data]
side_a = len(data)
side_b = len(data[0])
forrest = np.empty(shape=(side_a, side_b), dtype=np.int16)
for i in range(side_a):
    forrest[i] = list(data[i])

result = 0

max_lrud = 0
for i in range(side_a):
    for j in range(side_b):
        l, r, u, d = 0, 0, 0, 0
        tree = forrest[i][j]
        row_l = tree > forrest[i, 0:j]
        row_r = tree > forrest[i, j + 1 :]
        col_u = tree > forrest[0:i, j]
        col_d = tree > forrest[i + 1 :, j]
        for pos in reversed(row_l):
            if pos == True:
                l += 1
            else:
                l += 1
                break
        for col in col_u[::-1]:
            if col == True:
                u += 1
            else:
                u += 1
                break
        for pos in row_r:
            if pos == True:
                r += 1
            else:
                r += 1
                break
        for col in col_d:
            if col == True:
                d += 1
            else:
                d += 1
                break
        if (
            all(row_l) == True
            or all(row_r) == True
            or all(col_d) == True
            or all(col_u) == True
        ):
            result += 1
        if l * r * u * d > max_lrud:
            max_lrud = l * r * u * d
print(result)
print(max_lrud)
