import sys
import numpy as np
import re
import pandas as pd
def data_to_array(data):
    pts = np.array(
        [[a for a in map(int,line.split(","))] for line in data]
    )

    ar = np.zeros((np.amax(pts[:,0]) + 1, np.amax(pts[:,1]) + 1))
    ar[(pts[:,0], pts[:,1])] = 1
    return ar

def insts_to_list(data):
    ax_map = {"x":0, "y":1}
    res = []
    regex = "fold along ([y,x])=(\d*)"

    for line in data:
        ax,idx = re.match(regex, line).groups()
        res.append([ax_map[ax], int(idx)])
    return res

def fold(ar, ax, idx):
    if ax == 0:
        tofold = ar[idx + 1:,:] 
        tofold = tofold[::-1,:]
        ar = ar[:idx, :]
        ar += tofold
    else:
        tofold = ar[:,idx + 1:] 
        tofold = tofold[:,::-1]
        ar = ar[:,:idx]
        ar += tofold
    return ar

def main(path):
    with open(path) as f:
        rawpts, rawinsts = f.read().split("\n\n")

    print("==== PART ONE ====")

    ar = data_to_array(rawpts.splitlines())
    insts = insts_to_list(rawinsts.splitlines())
    for ax, idx in insts:
        ar = fold(ar, ax, idx)
        print(np.sum(ar != 0))



    print("==== PART TWO ====")
    test = np.full(ar.shape, " ")
    test[ar != 0] = "#"
    for line in test.T:
        print("".join(line))
if __name__ == "__main__":
    main(sys.argv[1])

