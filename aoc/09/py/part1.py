import sys
from itertools import product
import numpy as np
import pandas as pd

def expand_basin(df, bas, bas_idx):
    bas_x, bas_y = np.where(bas.values == bas_idx)
    bas_pts = list(zip(bas_x, bas_y))

    def check_bounds(x,y):
        xm, ym = bas.shape
        below = ((x < xm) and (y < ym))
        above = ((x >= 0) and (y >= 0))
        return (above and below)
    
    new_pts_count = 0
    for x,y in bas_pts:
        explore_pts = [(x + 1, y), (x-1,y), (x,y+1), (x,y-1)]
        for xn, yn in explore_pts:
            if check_bounds(xn,yn):
                if bas.isna().iloc[xn, yn]:
                    if df.iloc[xn,yn] != 9:
                        bas.iloc[xn,yn] = bas_idx
                        new_pts_count += 1
    
    if new_pts_count == 0:
        return df, bas, bas_idx
    else:
        expand_basin(df, bas, bas_idx)


def main(path):
    with open(path) as f:
        data = f.read().splitlines()
    data = [list(map(int, list(line))) for line in data]
    df = pd.DataFrame(data=data)
    
    print("===== PART ONE ========")
    dirs = [(1,0),(-1,0),(1,1),(-1,1)]
    shifts = [df.shift(i,axis=ax).fillna(10).astype(int) for i,ax in dirs]
    
    diffs = [df - x for x in shifts]
    
    total = sum([y < 0 for y in diffs])
    print((df + 1)[total == 4].sum().sum())

    print("======== PART TWO ========")
    # Assuming there is no local maxima that are not nine
    bas = pd.DataFrame(index = df.index, columns = df.columns, data = np.nan)
    for x,y in product(range(0, bas.shape[0]), range(0, bas.shape[1])):
        if df.iloc[x,y] == 9:
            bas.iloc[x,y] = -1

    bas_idx = 0
    while bas.isna().sum().sum() > 0:
        print(bas_idx)
        # Find a point that's not in a basin yet
        for x,y in product(range(0, bas.shape[0]), range(0, bas.shape[1])):
            if bas.isna().iloc[x,y]:
                bas.iloc[x,y] = bas_idx
                break

        expand_basin(df, bas, bas_idx)

        bas_idx += 1

    bas = bas.astype(int)

    print(bas)

    bas_counts = [(bas == i).sum().sum() for i in range(0, bas_idx)]
    bas_counts = sorted(bas_counts, reverse = True)
    print(bas_counts)

    res = 1
    for val in bas_counts[0:3]:
        res *= val
    print(res)

if __name__ == "__main__":
    main(sys.argv[1])
