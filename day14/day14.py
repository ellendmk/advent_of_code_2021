import numpy as np


def apply_insertion(start, rules):
    insert = [""] * len(start)
    for i in range(0, len(start) - 1):

        for a, b in rules:
            seq = start[i : i + 2]
            if a == seq:
                insert[i] += b
    new_start = ""
    for c in range(len(insert)):
        new_start = new_start + start[c] + insert[c]
    return new_start


def update_counts(counts, cur, v):
    if cur in counts.keys():
        counts[cur] += v
    else:
        counts[cur] = v
    return counts


def apply_insertion_faster(start, rules, counts):
    new_pairs = {}
    for k, v in start.items():
        if k in rules.keys():
            cur = rules[k]

            if k[0] + cur in new_pairs.keys():
                new_pairs[k[0] + cur] += start[k]
                counts = update_counts(counts, cur, v)
            else:
                new_pairs[k[0] + cur] = start[k]
                counts = update_counts(counts, cur, v)

            if cur + k[1] in new_pairs.keys():
                new_pairs[cur + k[1]] += start[k]
            else:
                new_pairs[cur + k[1]] = start[k]
        else:
            new_pairs[k] = start[k]

    return new_pairs, counts


# Part 1

f = open("test.txt").read()
f = open("in.txt").read()

start, rules_in = f.split("\n\n")

rules = set()
for l in rules_in.split("\n"):
    k, v = l.split(" -> ")
    rules.add(tuple([k, v]))

for i in range(10):
    start = apply_insertion(start, rules)

counts = {}
limits = [10000, 0]
for c in start:
    if c in counts.keys():
        continue
    else:
        counts[c] = start.count(c)
        if counts[c] < limits[0]:
            limits[0] = counts[c]
        if counts[c] > limits[1]:
            limits[1] = counts[c]

print(f"Answer part 1: {limits[1]-limits[0]}")

# Part 2
f = open("test.txt").read()
f = open("in.txt").read()

start, rules_in = f.split("\n\n")
counts = {}

rules = {}
for l in rules_in.split("\n"):
    k, v = l.split(" -> ")
    rules[k] = v

pairs_start = {}
for i in range(len(start) - 1):
    k = start[i : i + 2]
    if k in pairs_start.keys():
        pairs_start[k] += 1
    else:
        pairs_start[k] = 1

for i in start:
    if i in counts.keys():
        continue
    else:
        counts[i] = start.count(i)

for i in range(40):
    pairs_start, counts = apply_insertion_faster(pairs_start, rules, counts)

limits = [10 ** 30, 0]

for k, v in counts.items():
    if v < limits[0]:
        limits[0] = v
    if v > limits[1]:
        limits[1] = v

print(f"Answer part 2: {(limits[1]-limits[0])}")
