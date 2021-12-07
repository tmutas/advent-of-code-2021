import sys
import numpy as np

def find_min_pos(data, method = "p1"):
    fuel = np.iinfo(np.int64).max
    for i in range(np.amin(data), np.amax(data) + 1):
        if method == "p1":
            nfuel = np.abs(data - i).sum()
        elif method == "p2":
            nfuel = (np.power(data - i, 2) + np.abs(data - i)).sum()//2
        # Loss function has no local minima
        if nfuel >= fuel:
            return i - 1, fuel
        else:
            fuel = nfuel

def main(path):
    data = np.genfromtxt(path, delimiter = "," , dtype = np.int64)
    print("======== PART ONE ========")
    print(find_min_pos(data))
    print()
    print("======== PART TWO ========")
    print(find_min_pos(data, "p2"))

if __name__ == "__main__":
    main(sys.argv[1])