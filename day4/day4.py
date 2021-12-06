import numpy as np

BOARD_SIZE = 5
MARKER = -1
SUCCESS_SUM = MARKER * BOARD_SIZE
SUCCESS_PRODUCT = MARKER ** BOARD_SIZE
PART_1 = 1
PART_2 = 2


def play_bingo(calls, board_list, part):
    for i in range(len(calls)):
        for k in range(len(board_list)):
            b = board_list[k]
            b[np.where(b == calls[i])] = MARKER
            if (
                SUCCESS_PRODUCT in np.prod(b, axis=1)
                or SUCCESS_PRODUCT in np.prod(b, axis=0)
                or SUCCESS_SUM in np.sum(b, axis=1)
                or SUCCESS_SUM in np.sum(b, axis=0)
            ):
                if part == PART_1:
                    b[np.where(b == MARKER)] = 0
                    return (np.concatenate(b).sum(), calls[i])
                if part == PART_2:
                    if len(board_list) > 1:
                        board_list.pop(k)
                        return play_bingo(calls[i:], board_list, part)
                    b[np.where(b == MARKER)] = 0
                    return (np.concatenate(b).sum(), calls[i])


# Part 1
f = open("test.txt").read()
f = open("in.txt").read()
calls = [int(k) for k in f.split("\n")[0].split(",")]
boards = f.split("\n")[2:]

board_list = []

while len(boards):
    temp_arr = np.zeros([BOARD_SIZE, BOARD_SIZE])
    for k in range(5):
        temp_arr[k, :] = [int(i) for i in boards[k].split(" ") if i]
    board_list.append(temp_arr)
    boards = boards[6:]


final_score, last_call = play_bingo(calls, board_list, PART_1)

print(
    f"Answer part 1 - last call {last_call} and final score {final_score}: {last_call*final_score}"
)

# Part 2
f = open("test.txt").read()
f = open("in.txt").read()

calls = [int(k) for k in f.split("\n")[0].split(",")]
boards = f.split("\n")[2:]

board_list = []

while len(boards):
    temp_arr = np.zeros([BOARD_SIZE, BOARD_SIZE])
    for k in range(5):
        temp_arr[k, :] = [int(i) for i in boards[k].split(" ") if i]
    board_list.append(temp_arr)
    boards = boards[6:]


final_score, last_call = play_bingo(calls, board_list, PART_2)


print(
    f"Answer part 2 - last call {last_call} and final score {final_score}: {last_call*final_score}"
)
