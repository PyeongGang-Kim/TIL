def comb(idx =  0, arr = []):
    if len(arr) == N:
        vl2 = [False for _ in range(N)]
        Q = [arr[0]]
        vl2[0] = True
        front = 0
        rear = 1
        while front < rear:
            x, y = Q[front]
            front += 1
            for dx, dy in dr:
                tx, ty = x + dx, y + dy
                for i in range(N):
                    if not vl2[i] and arr[i][0] == tx and arr[i][1] == ty:
                        Q.append(arr[i])
                        rear += 1
                        vl2[i] = True
        if len(Q) == N:
            perm(arr, 0, 0)
        return
    for i in range(idx, 26-(N-len(arr))):
        arr.append(dl[i])
        comb(i+1, arr)
        arr.pop()


def perm(arr, idx, s):
    global r
    if s >= r:
        return

    if idx == N:
        r = min(r, s)
        return

    for i in range(idx, N):
        arr[i], arr[idx] = arr[idx], arr[i]
        perm(arr, idx+1, s + abs(arr[idx][0]-ml[idx][0]) + abs(arr[idx][1]-ml[idx][1]))
        arr[i], arr[idx] = arr[idx], arr[i]


dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
nl = [input() for _ in range(5)]
ml = []
dl = []
r = 0xfffffff
for j in range(5):
    for i in range(5):
        dl.append([i, j])
        if nl[j][i] == '*':
            ml.append([i, j])
N = len(ml)
comb()
print(r)