import sys
import re

import numpy as np

def data_to_array(data):
    ar = np.empty((len(data), 2, 2), dtype = np.int32)
    regex = "(\d*),(\d*) -> (\d*),(\d*)"
    for idx, line in enumerate(data):
        a1, a2, b1, b2 = re.match(regex, line).groups()
        ar[idx][0] = np.array([a1, a2], dtype = np.int32)
        ar[idx][1] = np.array([b1, b2], dtype = np.int32)
    
    return ar


def grid_size(ar):
    xmax = np.amax(ar[:,:,0].flatten())
    ymax = np.amax(ar[:,:,1].flatten())

    return xmax, ymax


def run_through_lines(ar, grid, diag = False):
    for line in ar:
        diff = line[1] - line[0]
        straight = 0 in diff
        if straight or diag:
            step = np.sign(diff)
            for i in range(0, np.amax(np.abs(diff)) + 1):
                grid[tuple(line[0] + step*i)] += 1

    return grid


def main(path):
    with open(path) as f:
        data = f.read().splitlines()

    ar = data_to_array(data)
    xmax, ymax = grid_size(ar)
    
    print("==== PART ONE ====")

    grid = np.zeros((xmax + 1, ymax + 1))
    grid = run_through_lines(ar, grid)

    print(np.sum(grid >= 2))

    print()
    print("==== PART TWO ====")

    grid = np.zeros((xmax + 1, ymax + 1))
    grid = run_through_lines(ar, grid, diag = True)

    print(np.sum(grid >= 2))


if __name__ == "__main__":
    path = "../input.txt" if len(sys.argv) <= 1 else sys.argv[1]
    main(path)

