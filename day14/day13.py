import numpy as np


def fold_paper(d, l, paper):
    if d == "x":
        # overwrite col
        paper[:, l] = -1
        left = paper[:, 0:l]
        right = np.flip(paper[:, l + 1 :], axis=1)
        right = np.pad(
            right, [(left.shape[0] - right.shape[0], 0), (0, 0)], constant_values=1
        )

        return left * right

    elif d == "y":
        # overwrite row
        paper[l, :] = -1
        top = paper[0:l, :]
        bott = np.flip(paper[l + 1 :, :], axis=0)
        bott = np.pad(
            bott, [(top.shape[0] - bott.shape[0], 0), (0, 0)], constant_values=1
        )
        return top * bott


# Part 1

f = open("test.txt").read()
f = open("in.txt").read()

coords_input, folds_input = f.split("\n\n")
max_size = [0, 0]
coords = []
for l in coords_input.split("\n"):
    c = [int(v) for v in l.split(",")]
    coords.append(c[::-1])
    if (c[1] + 1) > max_size[0]:
        max_size[0] = c[1] + 1
    if (c[0] + 1) > max_size[1]:
        max_size[1] = c[0] + 1
paper = np.ones(tuple(max_size))

for c in coords:
    paper[tuple(c)] = 0

folds = []
for p in folds_input.split("\n"):
    t = p.split(" ")[-1]
    d, v = t.split("=")
    folds.append([d, int(v)])


paper = fold_paper(folds[0][0], folds[0][1], paper)

print(f"Answer part 1: {(paper==0).sum().sum()}")

# Part 2
def print_code(paper):
    print()
    print()
    for i in range(paper.shape[0]):
        cur_row = ""
        for j in range(paper.shape[1]):
            if paper[i, j] == 1:
                cur_row += " "
            else:
                cur_row += "#"
        print(cur_row)
    print()
    print()


f = open("test.txt").read()
f = open("in.txt").read()

coords_input, folds_input = f.split("\n\n")
max_size = [0, 0]
coords = []
for l in coords_input.split("\n"):
    c = [int(v) for v in l.split(",")]
    coords.append(c[::-1])
    if (c[1] + 1) > max_size[0]:
        max_size[0] = c[1] + 1
    if (c[0] + 1) > max_size[1]:
        max_size[1] = c[0] + 1
paper = np.ones(tuple(max_size))

for c in coords:
    paper[tuple(c)] = 0

folds = []
for p in folds_input.split("\n"):
    t = p.split(" ")[-1]
    d, v = t.split("=")
    folds.append([d, int(v)])

for fold in folds:
    paper = fold_paper(fold[0], fold[1], paper)

print(f"Answer part 2:")

print_code(paper)
