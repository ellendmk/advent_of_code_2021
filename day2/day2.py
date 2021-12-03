# Part 1
# f = open('test.txt')
f = open("in.txt")
directs = f.read().split("\n")
f.close()

directs = [[k.split(" ")[0], int(k.split(" ")[1])] for k in directs]

posh = 0
posv = 0
aim = 0

direct_sign = {"forward": +1, "back": -1, "up": -1, "down": +1}

for d in directs:
    if d[0] in ("forward", "back"):
        posh = posh + direct_sign[d[0]] * d[1]
    if d[0] in ("up", "down"):
        posv = posv + direct_sign[d[0]] * d[1]

print(f"Answer part 1 pos_h {posh}, pos_v {posv} giving: {posh*posv}")

# Part 2
# f = open('test.txt')
f = open("in.txt")
directs = f.read().split("\n")
f.close()

directs = [[k.split(" ")[0], int(k.split(" ")[1])] for k in directs]

posh = 0
posv = 0
aim = 0

direct_sign = {"forward": +1, "back": -1, "up": -1, "down": +1}
aim_sign = {"down": +1, "up": -1, "forward": +1}


for d in directs:
    if d[0] in ("forward", "back"):
        posh = posh + direct_sign[d[0]] * d[1]
        posv = posv + aim * d[1]
    elif d[0] in ("up", "down"):
        aim = aim + direct_sign[d[0]] * d[1]

print(f"Answer part 1 pos_h {posh}, pos_v {posv} giving: {posh*posv}")
