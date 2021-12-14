import numpy as np


def apply_insertions(start, rules):
    i=0
    for 



# Part 1

f = open("test.txt").read()
# f = open("in.txt").read()

start, rules_in = f.split("\n\n")

rules=set()
for l in rules_in.split('\n'):
    k,v = l.split(' -> ')
    rules.add([tuple(k,v)])

print(rules,start)

print(f"Answer part 1: {0}")

# Part 2
