with open("../input.txt") as f:
    data = f.read().splitlines()

print(f"Number of lines: {len(data)}")
counts = [0]*len(data[0])
for line in data:
    for idx, val in enumerate(str(line)):
        counts[idx] += 1 if val == '1' else -1

print(f"Number of ones more per position: {counts}")

if 0 in counts:
    raise ValueError("Equal number of 0 and 1 occured")

gamma_list = [1 if i > 0 else 0 for i in counts]
epsilon_list = [0 if i > 0 else 1 for i in counts]

print(f"Gamma List: {gamma_list}")
print(f"Epsilon List: {epsilon_list}")

def binary_list_to_int(l):
    res = 0
    for idx, val in enumerate(l[::-1]):
        res += val*(2**idx)
    return res

gamma = binary_list_to_int(gamma_list)
epsilon = binary_list_to_int(epsilon_list)

print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")

print(f"Result: {gamma*epsilon}")

