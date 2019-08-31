from itertools import combinations

t = int(input())

for test_case in range(t):
    d, w, k = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(d)]


    def check():
        global d, w, k
        for col in range(w):
            flag = 0
            cnt = 1
            for row in range(d - 1):
                if d - row < k and cnt == 1:
                    break
                if data[row][col] == data[row + 1][col]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt == k:
                    flag = 1
                    break
            if not flag:
                return False
        return True


    def solve(depth):
        global d, w, res, data

        if depth == d:
            res = min(res, d)
            return
        comb = combinations(idx, depth)
        for c in comb:
            for j in range(2):
                for i in c:
                    data[i] = drug[j]
                if check():
                    res = min(res, depth)
                    return
                data = raw[:]


    data = raw[:]
    drug = [[0] * w, [1] * w]
    idx = list(range(d))
    visited = [0] * d
    res = float('inf')
    if check() or k <= 1:
        res = 0
    else:
        for i in range(1, d + 1):
            if i >= res:
                break
            solve(i)

    print('#{} {}'.format(test_case + 1, res))