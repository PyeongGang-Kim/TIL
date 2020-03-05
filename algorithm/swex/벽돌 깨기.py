from collections import deque


def per(arr, n, cnt):
    if n == N:
        global r
        r = min(r, cnt)
        return
    for i in range(W):
        carr = [a for a in [ar[:] for ar in arr]]
        per(carr, n+1, cnt - shoot(carr, i))


def shoot(arr, i):
    for j in range(H):
        if arr[j][i]:
            return crash(arr, i, j)
    return 0


def crash(arr, x, y):
    vl = [[0 for _ in range(W)] for _ in range(H)]
    vl[y][x] = 1
    Q = deque([[x, y, arr[y][x]]])
    arr[y][x] = 0
    cnt = 1
    while Q:
        x, y, K = Q.popleft()
        for k in range(1, K):
            for dx, dy in D:
                tx, ty = x + dx*k, y + dy*k
                if 0 <= tx < W and 0 <= ty < H and arr[ty][tx] and not vl[ty][tx]:
                    vl[ty][tx] = 1
                    cnt += 1
                    Q.append([tx, ty, arr[ty][tx]])
                    arr[ty][tx] = 0
    swap(arr)
    return cnt


def swap(arr):
    for i in range(W):
        for j in range(H-1, -1, -1):
            if not arr[j][i]:
                k = j
                for jj in range(j-1, -1, -1):
                    if arr[jj][i]:
                        arr[jj][i], arr[k][i] = arr[k][i], arr[jj][i]
                        k -= 1
                break


D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(H)]
    cnt = 0
    for j in range(H):
        for i in range(W):
            if nl[j][i]:
                cnt += 1
    r = cnt
    per(nl, 0, cnt)
    print('#{} {}'.format(tc, r))