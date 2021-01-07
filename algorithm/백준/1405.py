vl = [[0 for _ in range(30)] for _ in range(30)]
res = 0.0
D = [[1, 0, 0], [-1, 0, 1], [0, 1, 2], [0, -1, 3]]
cur_h = 1
dep = 0
def dfs(x=14, y=14):
    global cur_h, dep
    if dep == N:
        global res
        res += cur_h
        return
    for dx, dy, d in D:
        tx = x + dx
        ty = y + dy
        if not vl[ty][tx] and h[d] != 0:
            vl[ty][tx] = 1
            cur_h *= h[d]
            dep += 1
            dfs(tx, ty)
            cur_h /= h[d]
            vl[ty][tx] = 0
            dep -= 1

input_val = list(map(int, input().split()))
N = input_val[0]
h = [a/100 for a in input_val[1:]]

vl[14][14] = 1
dfs()
print(res)

