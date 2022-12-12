with open("day_10\d10_data.txt", "r") as file:
    data = file.readlines()
data = [line.strip() for line in data]

to_find = [20 + 40 * i for i in range(100)]

# sprite = ["." for _ in range(40)]
# sprite[0] = "#"
# sprite[1] = "#"
# sprite[2] = "#"
# crt = [[], [], [], [], [], []]

# result = 0
# cycle = 0
# x = 1
# crt_y = 0
# crt_x = 0


# def draw(crt_x, crt_y, crt, sprite):

#     if sprite[crt_x] == "#":
#         crt[crt_y].append("#")
#     else:
#         crt[crt_y].append(".")


# for line in data:
#     cycle += 1

#     if cycle in to_find:
#         result += cycle * x

#     if line.startswith("addx"):
#         value = line.split(" ")[-1]
#         cycle += 1

#         if cycle in to_find:
#             result += cycle * x
#         x += int(value)

# print(result)


class CPU:
    def __init__(self) -> None:
        self.cycle = 0
        self.register = 1
        self.crt = []
        self.r = 0
        self.sprite = ["." for _ in range(40)]
        self.sprite[0] = "#"
        self.sprite[1] = "#"
        self.sprite[2] = "#"

    def add_cycle(self):
        self.cycle += 1

    def add(self, value):
        self.register += value

    def result(self):
        self.r += self.cycle * self.register

    def check_cycle(self):
        if self.cycle in to_find:
            return True
        else:
            return False

    def draw_crt(self):
        crt_x = self.cycle % 40
        crt_y = self.cycle // 40
        if crt_y >= len(self.crt):
            self.crt.append([])
        if self.sprite[crt_x] == "#":
            self.crt[crt_y].append("#")
        elif self.sprite[crt_x] == ".":
            self.crt[crt_y].append(".")

    def move_sprite(self):
        self.sprite = ["." for _ in range(40)]
        if self.register > 0 and self.register < 39:
            self.sprite[self.register] = "#"
            self.sprite[self.register - 1] = "#"
            self.sprite[self.register + 1] = "#"
        elif self.register == 0:
            self.sprite[self.register] = "#"
            self.sprite[self.register + 1] = "#"
        elif self.register == 39:
            self.sprite[self.register] = "#"
            self.sprite[self.register - 1] = "#"


cpu = CPU()
for line in data:
    if line.startswith("noop"):

        cpu.add_cycle()
        cpu.draw_crt()
        if cpu.check_cycle():
            cpu.result()

    elif line.startswith("addx"):
        cpu.add_cycle()
        cpu.draw_crt()
        if cpu.check_cycle():
            cpu.result()
        cpu.add_cycle()
        cpu.draw_crt()
        if cpu.check_cycle():
            cpu.result()

        value = int(line.split(" ")[-1])
        cpu.add(value)

        cpu.move_sprite()

print(cpu.r)
for l in cpu.crt:
    print(l)
