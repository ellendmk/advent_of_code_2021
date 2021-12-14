import numpy as np


# Part 1
f = open("test.txt").read().split('\n')
# f = open("in.txt").read().split("\n")

paths_map = {}

for k in f:
    k,v = k.split('-')
    if k not in paths_map.keys():
        paths_map[k] = [v]
    else:
        paths_map[k].append(v)
    
    if v not in paths_map.keys():
        paths_map[v] = [k]
    else:
        paths_map[v].append(k)
    
def find_bad_ex(path_list):
    out = open('test_out.txt').read().split('\n')
    my_out = []
    for k in path_list:
        p = ','.join(k)
        my_out.append(p)
        if p not in out and k[-1]=='end':
            print(p)


def add_small_cave(path, cur_c, max_visits, part):
    counts = {cur_c:0}
    for c in set(path):
        if c.lower()==c:
            counts[c] = path.count(c)
    if part==1 and counts[cur_c]==0:
        return True
    elif part==2 and (max(counts.values()) + counts[cur_c])<=max_visits:
        return True
    return False


def all_paths_ended(paths):
    for k in paths:
        if k[-1]!='end':
            return False
    return True

def construct_paths(paths_map, max_visits=1, part=1):
    paths = [['start']]

    while all_paths_ended(paths)==False:
        cur_path = paths[0]
        paths = paths[1:]
        new_paths = []
        if cur_path[-1]=='end':
            paths.append(cur_path.copy())
            continue
        # elif cur_path[-1] not in paths_map.keys():
        #     continue
        for next_move in paths_map[cur_path[-1]]:
            if next_move!='start':
                # if next_move.lower()==next_move and part==1:
                #     if cur_path.count(next_move)>=max_visits:
                #         continue                
                if not add_small_cave(cur_path, next_move, max_visits, part):
                    # if count_small_caves(cur_path)>=max_visits:
                    continue

                new_paths.append(cur_path.copy()+[next_move])
            
        paths = paths+new_paths
    return paths
paths = construct_paths(paths_map)

print(f"Answer part 1: {len(paths)}")

# Part 2
f = open("test.txt").read().split('\n')
f = open("in.txt").read().split("\n")

paths_map = {}

for k in f:
    k,v = k.split('-')
    if k not in paths_map.keys():
        paths_map[k] = [v]
    else:
        paths_map[k].append(v)
    
    if v not in paths_map.keys():
        paths_map[v] = [k]
    else:
        paths_map[v].append(k)
    
paths = construct_paths(paths_map, 2, 2)

print(f"Answer part 2: {len(paths)}")