import numpy as np


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop_max(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] > self.queue[max][0]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

    def pop_min(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()


def valid_pt(k, range):
    for i in k:
        if i < range[0] or i > range[1]:
            return False
    return True


def Djikstra(start, cost):
    dist = {}
    prev = {}
    for i in range(cost.shape[0]):
        for j in range(cost.shape[1]):
            if i != 0 or j != 0:
                dist[(i, j)] = 10 ** 10
                prev[(i, j)] = 0

    dist[tuple(start)] = 0

    Q = PriorityQueue()

    Q.insert([0, start])

    while not Q.isEmpty():
        u = Q.pop_min()
        pt = u[1]
        up = [pt[0] - 1, pt[1]]
        down = [pt[0] + 1, pt[1]]
        left = [pt[0], pt[1] - 1]
        right = [pt[0], pt[1] + 1]
        positions = [
            k for k in [up, down, left, right] if valid_pt(k, [0, cost.shape[1] - 1])
        ]
        for p in positions:
            alt = dist[tuple(pt)] + cost[tuple(p)]
            if alt < dist[tuple(p)]:
                dist[tuple(p)] = alt
                prev[tuple(p)] = u
                Q.insert([alt, p])

    return dist, prev


# Part 1

f = open("test.txt").read().split("\n")
f = open("in.txt").read().split("\n")

risk_cave = np.ones(tuple([len(f), len(f)]))

for l in range(len(f)):
    risk_cave[l, :] = [int(k) for k in f[l]]

d, p = Djikstra([0, 0], risk_cave)

print(f"Answer part 1: {d[(risk_cave.shape[0]-1, risk_cave.shape[0]-1)]}")

# Part 2
def increase_map_size(cave):
    new_to_concat = [cave.copy()]
    for i in range(4):
        new_cave = new_to_concat[-1].copy() + 1
        new_cave = np.where(new_cave > 9, new_cave % 9, new_cave)
        new_to_concat.append(new_cave)
    new_array = np.concatenate(new_to_concat, axis=0)
    new_to_concat = [new_array.copy()]
    for i in range(4):
        new_cave = new_to_concat[-1].copy() + 1
        new_cave = np.where(new_cave > 9, new_cave % 9, new_cave)
        new_to_concat.append(new_cave)
    new_array = np.concatenate(new_to_concat, axis=1)
    return new_array


f = open("test.txt").read().split("\n")
f = open("in.txt").read().split("\n")

risk_cave = np.ones(tuple([len(f), len(f)]))

for l in range(len(f)):
    risk_cave[l, :] = [int(k) for k in f[l]]

risk_cave = increase_map_size(risk_cave)


d, p = Djikstra([0, 0], risk_cave)

print(f"Answer part 2: {d[(risk_cave.shape[0]-1, risk_cave.shape[0]-1)]}")
