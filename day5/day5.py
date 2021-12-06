from re import findall
import numpy as np
from collections import defaultdict


def extract_input(data):
    pos_list = []
    for line in data:
        x1, y1, x2, y2 = map(int, findall("[0-9]+", line))
        pos_list.append(((x1, y1, x2, y2)))
    return pos_list


def get_vent_count(pos_list, part=1):
    vent_cnt = defaultdict(int)

    for (x1, y1, x2, y2) in pos_list:
        dx, dy = map(np.sign, (x2 - x1, y2 - y1))
        if ((x1 == x2 or y1 == y2) and part == 1) or part != 1:

            while x1 != x2 + dx or y1 != y2 + dy:
                vent_cnt[(x1, y1)] += 1
                x1 = x1 + dx
                y1 = y1 + dy
    return vent_cnt


# Part 1
f = open("test.txt").read()
f = open("in.txt").read()

data = f.split("\n")

pos_list = extract_input(data)

print(f"Answer part 1: {sum([int(k>1) for k in get_vent_count(pos_list).values()])}")

# Part 2
f = open("test.txt").read()
f = open("in.txt").read()
data = f.split("\n")

pos_list = extract_input(data)

print(f"Answer part 2: {sum(k>1 for k in get_vent_count(pos_list, 2).values())}")
