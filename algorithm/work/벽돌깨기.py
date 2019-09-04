import sys
sys.stdin = open('asdf.txt')


def dfs(arr = []):
    global r
    if r == 0:
        return
    if len(arr) == N:
        arr2 = []
        for i in range(H):
            arr2.append(nl[i][:])
        for i in arr:
            C(i, arr2)
        tmp = 0
        for i in range(W):
            for j in range(H):
                if arr2[j][i]:
                    tmp += 1
        if r > tmp:
            r = tmp
        return
    for i in range(W):
        arr.append(i)
        dfs(arr)
        arr.pop()


def C(i, arr):
    st = []
    for j in range(H):
        if arr[j][i]:
            st = [[arr[j][i], i, j]]
            break
    vl = [[0 for _ in range(W)] for _ in range(H)]
    vl[j][i] = 1

    while st:
        P, x, y = st.pop()
        for l in range(1, P):
            for m in range(4):
                tx, ty = x + d[m][0] *l, y + d[m][1] *l
                if 0 <= tx < W and 0 <= ty < H and arr[ty][tx] and not vl[ty][tx]:
                    vl[ty][tx] = 1
                    if arr[ty][tx] != 1:
                        st.append([arr[ty][tx], tx, ty])
    for x in range(W):
        front = H - 1
        cnt = 0
        for h in range(H):
            if vl[h][x] or not arr[h][x]:
                cnt += 1
        for y in range(H - 1, 0, -1):
            if arr[y][x] and not vl[y][x]:
                arr[y][x], arr[front][x] = arr[front][x], arr[y][x]
                front -= 1
        for y in range(cnt):
            arr[y][x] = 0


d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(H)]
    r = H*W
    dfs()
    print('#{} {}'.format(t, r))