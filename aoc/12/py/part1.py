import sys
import re

import numpy as np
from collections import defaultdict

def data_to_dict(data):
    edges = defaultdict(list)
    for line in data:
        a,b = line.split("-")
        edges[a].append(b)
        edges[b].append(a)
    
    return edges

def explore_paths(stack, all_paths, edges, visited_twice):
    for nex in edges[stack[-1]]:
        if nex == "start":
            pass

        elif nex == "end":
            path = ",".join(stack)
            all_paths.append(path)

        elif nex.isupper() or nex not in stack:
            explore_paths(stack + [nex], all_paths, edges, visited_twice)
        
        elif nex in stack and not visited_twice:
            explore_paths(stack + [nex], all_paths, edges, True)

def main(path):
    with open(path) as f:
        data = f.read().splitlines()

    edges = data_to_dict(data)
    
    print("==== PART ONE ====")
    stack = ["start"]
    all_paths = []
    explore_paths(stack, all_paths, edges, True)
    print(len(all_paths))

    print("==== PART TWO ====")
    stack = ["start"]
    all_paths = []
    explore_paths(stack, all_paths, edges, False)
    print(len(all_paths))

if __name__ == "__main__":
    main(sys.argv[1])

