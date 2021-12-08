import sys

def get_mapping(inp):
    mp = {}
    for s in inp:
        if len(s) == 2:
            mp[s] = 1
        elif len(s) == 3:
            mp[s] = 7
        elif len(s) == 4:
            mp[s] = 4
        elif len(s) == 7:
            mp[s] = 8
    rev_mp = {v:s for s,v in mp.items()}

    for s in inp:
        if s not in mp.keys():
            if len(s) == 5:
                "Distinguish 2,3,5"
                if len(s & rev_mp[1]) == 2:
                    mp[s] = 3
                elif len(s & rev_mp[4]) == 3:
                    mp[s] = 5
                elif len(s & rev_mp[4]) == 2:
                    mp[s] = 2

            elif len(s) == 6:
                if len(s | rev_mp[1]) == 7:
                    mp[s] = 6
                elif len(s & rev_mp[4]) == 4:
                    mp[s] = 9
                else:
                    mp[s] = 0
    return mp
def main(path):
    with open(path) as f:
        data = f.read().splitlines()
    data = [map(str.split, l.split("|")) for l in data]
    
    data = [[list(map(str.strip, a)), list(map(str.strip,b))] for a,b in data]
    data = [[list(map(frozenset, a)), list(map(frozenset,b))] for a,b in data]

    print("======== PART ONE ========")
    count = 0
    for line in data:
        for inp in line[1]:
            if len(inp) in (2,4,3,7):
                count += 1
    print(count)

    print("======== PART TWO ========")
    vals = 0
    for line in data:
        m = get_mapping(line[0])
        rawval = [str(m[v]) for v in line[1]]
        valstr = "".join(rawval)
        val = int(valstr)
        vals += val
    print(vals)
if __name__ == "__main__":
    main(sys.argv[1])
