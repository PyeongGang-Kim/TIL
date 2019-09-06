import sys
sys.stdin = open('asdf.txt')


def pt(i, j):
    tmp = []
    for i in range(8):
        tx, ty = i + dr[i][0], j + dr[i][1]
        if 0 <= tx < N and 0 <= ty < N:
            tmp.append([tx, ty])
    return tmp



dr = [[0, 1], [1, 1], [1, 0], [1, -1], [-1, -1], [-1, 1], [-1, 0], [0, -1]]

N, M, K = map(int, input().split())
nl = [[[i, [], i] for i in list(map(int, input().split()))] for _ in range(N)]
tr = [list(map(int, input().split())) for _ in range(M)]
for tree in tr:
    nl[tree[0]-1][tree[1]-1][1].append(-tree[2])
print(nl)
time = 0
while K > time:
    for ny in range(N):
        for nx in range(N):
            if not nl[ny][nx][1]:
                nl[ny][nx][0] += nl[ny][nx][2]
                continue
            tmp = 0
            s = nl[ny][nx][0]
            tmp2 = len(nl[ny][nx][1])
            tmp3 = 0
            i = 0
            while i < tmp2:
                tmp += (time - nl[ny][nx][1][i])
                if tmp > s:
                    break
                i += 1

            for _ in range(tmp2 - i):
                tmp3 += (time - nl[ny][nx][1].pop()) // 2
            nl[ny][nx][0] = tmp3 + nl[ny][nx][2]
    time += 1
    pts = []

    for ny in range(N):
        for nx in range(N):
            if nl[ny][nx][1]:
                #나무 심어주기 좌표, 나이(time+1)
                for tree in nl[ny][nx][1]:
                    pts = pts + pt(nx, ny)

    for tree in pts:
        nl[tree[1]][tree[0]][1].append(time-1)

cnt = 0
for _ in range(N):
    for __ in range(N):
        cnt += len(nl[ny][nx][1])
print(cnt)
