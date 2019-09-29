from collections import deque
'''
집 셋([거리, 치킨집좌표] 리스트 bfs로 접근하면 오름차순 됨.
치킨집 셋
M개 남기는 조합
각 집에서 거리와 치킨집
사라진 치킨집일때만 거리를 bfs로 새로 구함
모든 집에서 각 치킨 집까지의 거리들을 bfs로 저장해놓음.
=> 시간초과. 원인 분석해보니 조합을 이상하게 만들고 있었음.

%%조합이 제대로 만들어졌는지 확인하고 시작하기.
'''
def bfs(i, j):
    vl = [[0 for _ in range(N)] for _ in range(N)]
    Q = deque([[i, j]])
    vl[j][i] = 1
    hl[(i, j)] = []
    while Q:
        x, y = Q.popleft()
        for dx, dy in d:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < N and not vl[ty][tx]:
                vl[ty][tx] = 1
                Q.append([tx, ty])
                if nl[ty][tx] == 2:
                    ds = abs(i-tx) + abs(j-ty)
                    hl[(i, j)].append([ds, tx, ty])

def comb(arr=[], idx = 0):
    global R
    if len(arr) == M:
        tmpcl = set()
        coun = 0
        for i in arr:
            tmpcl.add(cl[i])
        for cls in hl.values():
            for clt in cls:
                if (clt[1], clt[2]) in tmpcl:
                    coun += clt[0]
                    break
            if coun > R:
                break
        if coun < R:
            R = coun
        return
    for i in range(idx,  C - (M-len(arr))+1):
        arr.append(i)
        comb(arr, i+1)
        arr.pop()



d = [[0, 1], [0, -1], [-1, 0], [1, 0]]
N, M = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
hl = {}
cl = []
ht = set()
R = 0xfffffff
for i in range(N):
    for j in range(N):
        if nl[j][i]:
            if nl[j][i] & 1:
                ht.add((i, j))
            else:
                cl.append((i, j))

C = len(cl)
for h in ht:
    bfs(*h)
comb()
print(R)