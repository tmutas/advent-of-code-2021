import sys

def load_input(path):
    with open(path) as f:
        data = f.read().splitlines()
    ar = list(map(int, data[0].split(",")))
    return ar

def count_list(ar):
    cts = [0]*9
    for idx, _ in enumerate(cts):
        for i in ar:
            if i == idx:
                cts[idx] += 1
    return cts

def shift_day(cts):
    new = [0]*9
    for idx, val in enumerate(cts):
        new_idx = (idx - 1) % len(cts)
        new[new_idx] = val
    return new

def main(path):
    print("==== PART ONE ====")
    ar = load_input(path)
    days = 80
    for i in range(0,days):
        ar = list(map(lambda x:x - 1, ar))
        for idx, val in enumerate(ar):
            if val == -1:
                ar[idx] = 6
                ar.append(8)
    print(len(ar))

    print("==== PART TWO ====")
    ar = load_input(path)
    cts = count_list(ar)
    days_two = 256
    for i in range(0,days_two):
        cts = shift_day(cts)
        cts[6] += cts[8]
        
    sum = 0
    for val in cts:
        sum += val
    print(sum)


if __name__ == "__main__":
    main(sys.argv[1])
