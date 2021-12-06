import numpy as np

DAYS = 256
# slow
def time_travel(fish, days):
    fish[fish == -1] = 6
    fish = fish - 1
    fish_to_add = sum(fish == -1)
    fish = np.append(fish, [8] * fish_to_add)

    if days - 1 == 0:
        return fish
    return time_travel(fish, days - 1)


# faster
def time_travel_gest(gest_days, days):
    gest_days[6] += gest_days[-1]
    gest_days[-1] = 0
    for k in range(0, max(gest_days.keys()) + 1):
        gest_days[k - 1] = gest_days[k]
    gest_days[8] = gest_days[-1]

    if days - 1 == 0:
        return gest_days
    return time_travel_gest(gest_days, days - 1)


# Part 1
# f = open("test.txt").read()
f = open("in.txt").read()

gest_days = {k: 0 for k in range(-1, 9)}
for k in f.split(","):
    gest_days[int(k)] += 1

final = time_travel_gest(gest_days, 80)

print(f"Answer part 1: {sum(list(final.values()))}")


# Part 2
# f = open("test.txt").read()
f = open("in.txt").read()

gest_days = {k: 0 for k in range(-1, 9)}
for k in f.split(","):
    gest_days[int(k)] += 1

final = time_travel_gest(gest_days, DAYS)

print(f"Answer part 2: {sum(list(final.values()))}")
