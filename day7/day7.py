import numpy as np


def triangle_num(n):
    return n * (n + 1) / 2


# Part 1
f = open("test.txt").read()
f = open("in.txt").read()

pos_arr = np.array([int(k) for k in f.split(",")])

min_fuel = 10 ** 10
for k in range(0, max(pos_arr)):
    min_fuel = min(abs(k - pos_arr).sum(), min_fuel)
ans = 0

print(f"Answer part 1: {min_fuel}")

# Part 2
f = open("test.txt").read()
f = open("in.txt").read()

pos_arr = np.array([int(k) for k in f.split(",")])
min_fuel = 10 ** 10
for k in range(0, max(pos_arr)):
    tn = triangle_num(abs(k - pos_arr))
    min_fuel = min(tn.sum(), min_fuel)

print(f"Answer part 2: {min_fuel}")
