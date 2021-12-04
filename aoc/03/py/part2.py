with open("../input.txt") as f:
    data = f.read().splitlines()


def reduce(li, bit, most=1, least=0):
    print(f"{len(li)}")
    if len(li) == 1:
        return li
    lists = {0: [], 1: []}
    counts = 0
    for line in li:
        val = int(line[bit])
        counts += 1 if val == 1 else -1
        lists[val].append(line)
    final_list = lists[most] if counts >= 0 else lists[least]

    return reduce(final_list, bit + 1, most, least)


v1 = reduce(data, 0, 1, 0)
v2 = reduce(data, 0, 0, 1)
print(v1)
print(v2)
print("==========")
print(int(v1[0], 2))
print(int(v2[0], 2))
print("==========")
print(int(v1[0], 2) * int(v2[0], 2))
