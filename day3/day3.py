import numpy as np


def get_common_bits(arr):
    diag_sum = arr.sum(axis=0)
    return {
        "most": (diag_sum >= (arr.shape[0] / 2)).astype(int),
        "least": (diag_sum < (arr.shape[0] / 2)).astype(int),
    }


def filter_array(arr, bits, least, part):
    for i in range(len(bits)):
        arr = arr[np.where(arr[:, i] == bits[i])]
        if part == 2:

            bits = get_common_bits(arr)["least" if least else "most"]
        if arr.shape[0] == 1:
            return arr
    return arr


# Part 1
PART = 1
f = open("test.txt").read()
f = open("in.txt").read()

temp_in = [k for k in f.split("\n")]

diag_rep = np.zeros([len(temp_in), len(temp_in[0])])
for i in range(len(temp_in)):
    diag_rep[i, :] = [int(v) for v in temp_in[i]]

# get most common bits
gamma = "".join([str(x) for x in get_common_bits(diag_rep)["most"]])
gamma_dec = int(gamma, 2)

# get least common bits
eps = "".join([str(x) for x in get_common_bits(diag_rep)["least"]])
eps_dec = int(eps, 2)


print(
    f"Answer part 1 using gamma {gamma_dec} and epsilon {eps_dec}: {gamma_dec*eps_dec}"
)

# Part 2
PART = 2
# f = open('test.txt').read()
f = open("in.txt").read()

temp_in = [k for k in f.split("\n")]

diag_rep = np.zeros([len(temp_in), len(temp_in[0])])
for i in range(len(temp_in)):
    diag_rep[i, :] = [int(v) for v in temp_in[i]]

# get most common bits
most = get_common_bits(diag_rep)["most"]
ogr = filter_array(diag_rep.copy(), most, 0, PART)
ogr = "".join([str(int(x)) for x in ogr[0]])
ogr_dec = int(ogr, 2)

least = get_common_bits(diag_rep)["least"]
csr = filter_array(diag_rep.copy(), least, 1, PART)
csr = "".join([str(int(x)) for x in csr[0]])
csr_dec = int(csr, 2)

print(f"Answer part 2 using ogr {ogr_dec} and csr {csr_dec}: {ogr_dec*csr_dec}")
