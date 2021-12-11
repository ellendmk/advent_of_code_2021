import numpy as np


dirs = {
    "u": (-1, 0),
    "d": (+1, 0),
    "l": (0, -1),
    "r": (0, +1),
    "ul": (-1, -1),
    "ur": (-1, +1),
    "dl": (+1, -1),
    "dr": (+1, +1),
}


def update_energy(je):
    # check flashes
    flashes = set()
    while (je >= 9).sum().sum() > 0:

        for i in range(je.shape[0]):
            for j in range(je.shape[1]):
                if je[i, j] >= 9 and (i, j) not in flashes:
                    flashes.update([(i, j)])
                    for v in dirs.values():
                        pt = (i + v[0], j + v[1])
                        if (pt[0] < je.shape[0] and pt[0] >= 0) and (
                            pt[1] < je.shape[1] and pt[1] >= 0
                        ):
                            je[pt] += 1

        for k in flashes:
            je[k] = 0

    je = je + 1
    for k in flashes:
        je[k] = 0
    return je, len(flashes)


# Part 1
# f = open("test.txt").read().split('\n')
f = open("in.txt").read().split("\n")
je = []
for l in f:
    je.append([int(k) for k in l])

je = np.array(je)
total_flashes = 0
for k in range(100):
    je, new_flashes = update_energy(je)
    total_flashes = total_flashes + new_flashes
print(f"Answer part 1: {total_flashes}")

# Part 2
f = open("test.txt").read().split("\n")
f = open("in.txt").read().split("\n")

je = []
for l in f:
    je.append([int(k) for k in l])

je = np.array(je)

flash_round = 1
while True:
    je, flashes = update_energy(je)
    if flashes == je.shape[0] * je.shape[1]:
        break
    flash_round += 1
print(f"Answer part 2: {flash_round}")
