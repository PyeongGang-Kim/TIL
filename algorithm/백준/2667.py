from collections import deque
'''
모든 좌표를 2중포문을 이용해 탐색한다.
만약 방문 안했으면서 현재 위치의 값이 1인 경우 해당 위치에서 bfs를 실시한다.
bfs하는 동안에 카운팅 해주고 그 값을 리턴
리턴받은 값을 결과 리스트(r)에 추가해준다.
결과 리스트의 길이를 출력한다.
결과 리스트를 소팅한 후 순차적으로 출력한다.
'''

def bfs(i, j):
    Q = deque([[i, j]])
    cnt = 0
    vl[j][i] = 1
    while Q:
        x, y = Q.popleft()
        cnt += 1
        for dx, dy in d:
            tx, ty = x+dx, y+dy
            if 0 <= tx < n and 0 <= ty < n and not vl[ty][tx] and nl[ty][tx] == '1':
                vl[ty][tx] = 1
                Q.append([tx, ty])
    r.append(cnt)


d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
n = int(input())
nl = [input() for _ in range(n)]
vl = [[0 for _ in range(n)] for _ in range(n)]
r = []
for j in range(n):
    for i in range(n):
        if nl[j][i] == '1' and not vl[j][i]:
            bfs(i, j)
r.sort()
print(len(r))
[print(i) for i in r]