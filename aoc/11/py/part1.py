import sys
from itertools import product
import numpy as np
from numpy.core.numeric import full
import pandas as pd

def step(df, mask):
    def xymask(x,y,m):
        return m.shift(x - 1, axis=0).shift(y - 1, axis=1).fillna(0)
    
    count = 0
    df += 1
    flashed = np.zeros(df.shape) != 0

    while np.sum(df.values > 9) != 0:
        flashed_now = df.values > 9
        flashed = flashed | flashed_now
        count += np.sum(flashed_now)
        
        xx,yy = np.where(flashed_now)
        full_mask = np.zeros(df.shape)
        for x,y in zip(xx,yy):
            full_mask += xymask(x,y,mask)
        
        df += full_mask
        df[flashed] = 0

    return df, count

def main(path):
    with open(path) as f:
        data = f.read().splitlines()
    data = [list(map(int, list(line))) for line in data]
    df = pd.DataFrame(data=data)

    mask = pd.DataFrame(np.zeros(df.shape))
    mask.iloc[:3,:3] = 1
    mask.iloc[1,1] = 0
    print("===== PART ONE ========")
    print(df)
    count = 0
    days = 0
    while True:
        df, new_count = step(df, mask)
        count += new_count
        days += 1
        if days == 100:
            print(f"Part One: {count}")
        if new_count == df.size:
            print(f"Part Two: {days}")
            break

    print("======== PART TWO ========")


if __name__ == "__main__":
    main(sys.argv[1])
