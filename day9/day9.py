import numpy as np


def is_low_point(centre, pts):
    for k in pts:
        if centre < k:
            continue
        else:
            return False
    return True


def get_low_points(h_map):
    low_pts = []
    low_pts_coords = []
    for i in range(h_map.shape[0]):
        for j in range(h_map.shape[1]):
            up = sorted((0, i - 1, h_map.shape[0] - 1))[1]
            down = sorted((0, i + 1, h_map.shape[0] - 1))[1]
            left = sorted((0, j - 1, h_map.shape[1] - 1))[1]
            right = sorted((0, j + 1, h_map.shape[1] - 1))[1]
            pts_to_check = []
            for k in [[up, j], [down, j], [i, left], [i, right]]:
                if k != [i, j]:
                    pts_to_check.append(h_map[k[0], k[1]])
            if is_low_point(h_map[i, j], pts_to_check,):
                low_pts.append(h_map[i, j])
                low_pts_coords.append([i, j])
    return low_pts, low_pts_coords


# Part 1
f = open("test.txt").read()
f = open("in.txt").read()

h_map = []
for l in f.split("\n"):
    h_map.append([int(n) for n in l])

h_map = np.array(h_map)

low_pts, _ = get_low_points(h_map)

print(f"Answer part 1: {sum(k+1 for k in low_pts)}")

# Part 2
def dist(a, b):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def find_basins(low_point_coords, h_map):
    basins = [[tuple(k)] for k in low_point_coords]
    while (
        sum([len(k) for k in basins])
        < h_map.shape[0] * h_map.shape[1] - (h_map == 9).sum().sum()
    ):
        for b in range(len(basins)):
            pt = 0
            print(
                sum([len(k) for k in basins]),
                "/",
                h_map.shape[0] * h_map.shape[1] - (h_map == 9).sum().sum(),
                sum([len(k) for k in basins])
                / (h_map.shape[0] * h_map.shape[1] - (h_map == 9).sum().sum())
                * 100,
                end="\r",
            )

            while pt < len(basins[b]):
                for i in range(h_map.shape[0]):
                    for j in range(h_map.shape[1]):
                        if (i, j) in basins[b]:
                            continue
                        if h_map[i, j] < 9 and dist((i, j), basins[b][pt]) < np.sqrt(2):
                            basins[b].append((i, j))
                pt += 1
    return basins


def is_inside(node_val, filler):
    # print('------------is_inside-----------------')
    # print(node_val, filler)
    if node_val == 9 or node_val == filler:
        return False
    return True


def flood_fill(node, h_map, filler):
    if is_inside(h_map[node[0], node[1]], filler):
        h_map[node[0], node[1]] = filler
    else:
        return h_map
    # print(h_map[node[0], node[1]])
    up = [sorted((0, node[0] - 1, h_map.shape[0] - 1))[1], node[1]]
    down = [sorted((0, node[0] + 1, h_map.shape[0] - 1))[1], node[1]]
    left = [node[0], sorted((0, node[1] - 1, h_map.shape[1] - 1))[1]]
    right = [node[0], sorted((0, node[1] + 1, h_map.shape[1] - 1))[1]]
    # print(tuple(up)!=tuple(node), up, node)
    # print(node)
    # input()
    if up[0] != node[0] or up[1] != node[1]:
        # print('going up')
        h_map = flood_fill(up, h_map, filler)
    if down[0] != node[0] or down[1] != node[1]:
        # print('going down')
        h_map = flood_fill(down, h_map, filler)
    if left[0] != node[0] or left[1] != node[1]:
        # print('going left')
        h_map = flood_fill(left, h_map, filler)
    if right[0] != node[0] or right[1] != node[1]:
        # print('going right')
        h_map = flood_fill(right, h_map, filler)
    # print(h_map)
    # input()
    return h_map


f = open("test.txt").read()
f = open("in.txt").read()

h_map = []
for l in f.split("\n"):
    h_map.append([int(n) for n in l])

h_map = np.array(h_map)
_, low_point_coords = get_low_points(h_map)
#### slower
# Need to make this faster - flood fill algorithm
# basins = find_basins(low_point_coords, h_map)
##### faster
basins = []
basin_sizes = []
for k in range(len(low_point_coords)):
    basins.append(flood_fill(low_point_coords[k], h_map, k * -1 - 1))
    basin_sizes.append((basins[-1] == k * -1 - 1).sum().sum())
print(f"Answer part 2: {np.prod(sorted(basin_sizes)[-3:])}")
