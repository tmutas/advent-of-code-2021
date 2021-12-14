import sys
import re
from collections import Counter
import numpy as np

def data_to_array(data):
    regex = "([A-Z]{2}) -> ([A-Z]{1})"
    return {a:b for a,b in [re.match(regex, line).groups() for line in data]}


def main(path):
    with open(path) as f:
        data = f.read().splitlines()
    init_st = data[0]
    rules = data_to_array(data[2:])
    print("======== PART ONE ========")
    steps = 10

    for i in range(steps):
        init_st = "".join(
            [c + rules.get(init_st[i:i+2], "") for i, c in enumerate(init_st)]
        )
    counts = Counter(init_st).most_common()
    print(counts[0][1] - counts[-1][1])

    print("======== PART TWO ========")
    init_st = data[0]
    pairs = Counter([init_st[i:i+2] for i in range(len(init_st) - 1)])
    letters = Counter(init_st)
    steps2 = 40
    for i in range(steps2):
        new = Counter(pairs)
        for p, pc in pairs.items():
            if p in rules:
                a, c = tuple(p)
                b = rules[p]
                letters[b] += pc
                new[p] -= pc
                new[a+b] += pc
                new[b+c] += pc
        pairs = new

    counts = letters.most_common()
    print(counts[0][1] - counts[-1][1])

if __name__ == "__main__":
    main(sys.argv[1])

