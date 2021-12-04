import numpy as np


def to_array(bds):
    ar = np.zeros((5, 5), dtype=np.int8)
    for row_i, row in enumerate(bds):
        for col_i in range(0, 5):
            st = col_i*3
            s = row[st:st + 2].strip()
            ar[row_i][col_i] = int(s)
    return ar


def find_num(b, i):
    # Returns coordinates as 1-d ve
    res = np.where(b == i)
    return None if res[0].size == 0 else np.hstack(res)


def run_numbers(nums, boards):
    marked = [np.zeros((5, 5), dtype=np.int8) for i in boards]

    for i in nums:
        for bidx, b in enumerate(boards):
            marked[bidx][b == i] = 1
            for ax in [0, 1]:
                if 5 in np.sum(marked[bidx], axis=ax):
                    return (bidx, marked[bidx], i)


def run_last(nums, boards):
    marked = [np.zeros((5, 5), dtype=np.int8) for i in boards]
    won = []
    for i in nums:
        for bidx, b in enumerate(boards):
            if bidx not in won:
                marked[bidx][b == i] = 1
                for ax in [0, 1]:
                    if 5 in np.sum(marked[bidx], axis=ax):
                        won.append(bidx)
                        if len(won) == len(boards):
                            return (bidx, marked[bidx], i)
                        else:
                            break

def main():
    with open("../input.txt") as f:
        data = f.read().splitlines()

    # Save list of drawn numbers and remove first two lines
    nums = list(map(int, data.pop(0).split(",")))
    data.pop(0)

    # Load boards
    raw_boards = []
    cur_board = []
    for line in data:
        if line == "":
            raw_boards.append(cur_board)
            cur_board = []
        else:
            cur_board.append(line)
    raw_boards.append(cur_board)

    # Transform boards to numpy
    boards = [to_array(i) for i in raw_boards]

    # Go through numbers
    print("==== PART ONE ====")
    bidx, marked, num = run_numbers(nums, boards)
    print(np.sum(boards[bidx][marked == 0]) * num)
    
    print()
    print("==== PART TWO ====")
    bidx, marked, num = run_last(nums, boards)
    print(np.sum(boards[bidx][marked == 0]) * num)


if __name__ == "__main__":
    main()
