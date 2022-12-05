with open("day_4\d4_data.txt", "r") as file:
    lines = file.readlines()
pairs = 0
part = 0
for line in lines:
    l, r = line.split(",")
    ll, lr = l.split("-")
    rl, rr = r.split("-")
    ll, lr, rl, rr = int(ll), int(lr), int(rl), int(rr)
    if ll <= rl and lr >= rr or ll >= rl and lr <= rr:
        pairs += 1

    l = set(range(ll, lr + 1))
    r = set(range(rl, rr + 1))
    f = l & r

    if f:
        part += 1

print(pairs)
print(part)
