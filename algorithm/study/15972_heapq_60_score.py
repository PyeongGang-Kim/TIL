import heapq
'''
push하는데 시간이 상당히 들어가기 때문에 힙에 데이터 넣는것을 최소화 해야 한다.
+ 힙을 사용할 필요가 없는 문제였다면 그냥 bfs가 더 나을 수 있다.
'''
N, M, H = map(int, input().split())
nl = [[[H, [0, 0, 0, 0]] for _ in range(M)] for _ in range(N)]
tmp = list(map(int, input().split()))
Q = []
heapq.heapify(Q)


for m in range(M):
    nl[0][m][1][0] = tmp[m]
    if tmp[m] != -1:
        nl[0][m][0] = min(nl[0][m][0], tmp[m])
        heapq.heappush(Q, [nl[0][m][0], m, 0])
for n in range(1, N):
    tmp = list(map(int, input().split()))
    for m in range(M):
        nl[n-1][m][1][2] = tmp[m]
        nl[n][m][1][0] = tmp[m]
tmp = list(map(int, input().split()))
for m in range(M):
    nl[-1][m][1][2] = tmp[m]
    if tmp[m] != -1:
        nl[-1][m][0] = min(nl[-1][m][0], tmp[m])
        heapq.heappush(Q, [nl[-1][m][0], m, N-1])

for n in range(N):
    tmp = list(map(int, input().split()))
    nl[n][0][1][3] = tmp[0]
    if tmp[0] != -1:
        nl[n][0][0] = min(nl[n][0][0], tmp[0])
        heapq.heappush(Q, [nl[n][0][0], 0, n])

    for m in range(1, M):
        nl[n][m-1][1][1] = tmp[m]
        nl[n][m][1][3] = tmp[m]
    nl[n][-1][1][1] = tmp[-1]
    if tmp[-1] != -1:
        nl[n][-1][0] = min(nl[n][-1][0], tmp[-1])
        heapq.heappush(Q, [nl[n][-1][0], M-1, n])


dr = [[0, -1], [1, 0], [0, 1], [-1, 0]]
while Q:
    h, x, y = heapq.heappop(Q)
    if nl[y][x][0] > h:
        continue
    for idx, height in enumerate(nl[y][x][1]):
        if height != -1:
            tx, ty = x + dr[idx][0], y + dr[idx][1]
            if 0 <= tx < M and 0 <= ty < N and nl[ty][tx][0] > height and (h <= height or nl[ty][tx][0] > h):
                tmp = max(height, h)
                nl[ty][tx][0] = tmp
                heapq.heappush(Q, [tmp, tx, ty])
r = 0
for j in range(N):
    for i in range(M):
        r += nl[j][i][0]
print(r)