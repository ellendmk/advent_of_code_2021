import numpy as np
import re

sequences = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


def generate_patterns(sequences):
    patterns = {}
    for i in range(10):
        s = sequences[i]
        cur_pat = []
        for v in [1, 4, 7, 8]:
            cur_pat.append(sum(n in s for n in sequences[v]))
        patterns[tuple(cur_pat)] = i
    return patterns


OVERLAP_PATTERNS = generate_patterns(sequences)


def get_1478(digits):
    dig1 = ""
    dig4 = ""
    dig7 = ""
    dig8 = ""
    for k in digits:
        if len(k) == 7:
            dig8 = k
        elif len(k) == 2:
            dig1 = k
        elif len(k) == 4:
            dig4 = k
        elif len(k) == 3:
            dig7 = k
    return dig1, dig4, dig7, dig8


# Part 1
f = open("test.txt").read()
f = open("in.txt").read()

sig_pat = []
digit = []
for line in f.split("\n"):
    digit.append([k for k in line.split(" | ")[1].split(" ") if k])
    sig_pat.append([k for k in line.split(" | ")[0].split(" ") if k])

id_sigs = []

for k in range(len(digit)):
    cur_row = []
    for n in digit[k]:
        if len(n) == 4 or len(n) == 2 or len(n) == 7 or len(n) == 3:
            cur_row.append(n)

    id_sigs += cur_row

print(f"Answer part 1: {len(id_sigs)}")

# Part 2
def get_pattern(cur_digit, digits):
    pattern = []
    for v in digits:
        count = 0
        for c in cur_digit:
            if c in v:
                count += 1
        pattern.append(count)
    return pattern


f = open("test.txt").read()
f = open("in.txt").read()
total = 0
digit = []
sig_pat = []
for line in f.split("\n"):
    digit.append([k for k in line.split(" | ")[1].split(" ") if k])
    sig_pat.append([k for k in line.split(" | ")[0].split(" ") if k])

for k in range(0, len(digit)):
    dig1, dig4, dig7, dig8 = get_1478(digit[k] + sig_pat[k])
    this_digit = ""
    for n in digit[k]:
        pattern = tuple(get_pattern(n, [dig1, dig4, dig7, dig8]))
        if pattern in OVERLAP_PATTERNS.keys():
            this_digit += str(OVERLAP_PATTERNS[pattern])
    total += int(this_digit)

print(f"Answer part 2: {total}")
