import sys

def main(path):
    with open(path) as f:
        data = f.read().splitlines()
    op = {"(" : ")", "[" : "]", "{" : "}", "<":">"}
    vals = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
    vals2 = {"(" : 1, "[" : 2, "{" : 3, "<" : 4}
    print("===== PART ONE ========")
    score = 0
    for line in data:
        stack = []
        for c in line:
            if c in op:
                stack.append(c)
            else:

                if c != op[stack.pop()]:
                    score += vals[c]
                    break

    print(score)
    print("======== PART TWO ========")
    score2 = []
    for line in data:
        stack = []
        faulty = False
        for c in line:
            if c in op:
                stack.append(c)
            else:
                if c != op[stack.pop()]:
                    faulty = True
        line_score = 0
        if not faulty:
            for v in stack[::-1]:
                line_score *= 5
                line_score += vals2[v]
            score2.append(line_score)
    score2 = sorted(score2)

    print(score2[len(score2) // 2])

if __name__ == "__main__":
    main(sys.argv[1])