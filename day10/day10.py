import numpy as np

# Part 1
# f = open("test.txt").readlines()
f = open("in.txt").read().split('\n')
SCORES={')':3,'}':1197,']':57,'>':25137}
score = 0

for line in f:
    brackets = [] 
    for c in line:

        if c=='[':
            brackets.append(']')
        elif c=='(':
            brackets.append(')')
        elif c =='{':
            brackets.append('}')
        elif c=='<':
            brackets.append('>')
        elif c!=brackets[-1]:
            score+=SCORES[c]
            break
        else:
            brackets.pop()
        

print(f"Answer part 1: {score}")

# Part 2
# f = open("test.txt").read().split('\n')
f = open("in.txt").read().split('\n')

SCORES={')':1,'}':3,']':2,'>':4}

all_scores=[]
for line in f:
    score = 0
    brackets = [] 
    for c in line:
        if c=='[':
            brackets.append(']')
        elif c=='(':
            brackets.append(')')
        elif c =='{':
            brackets.append('}')
        elif c=='<':
            brackets.append('>')
        elif c!=brackets[-1]:
            brackets=[]
            break
        else:
            brackets.pop()
    if len(brackets)>0:
        for k in brackets[::-1]:
            score = score*5 + SCORES[k]
        all_scores.append(score)

print(f"Answer part 2: {sorted(all_scores)[int(len(all_scores)/2)]}")
