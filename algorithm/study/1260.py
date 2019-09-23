import sys
from collections import deque
'''
dfs는 스택에 추가되고 작은것부터 접근해야 하므로 큰 값부터 처례로 넣어준다
=> 갈 수 있는 곳이 정렬된 상태로 주어져야 함.

각 간선들을 키(정점의 번호): 밸류(해당 정점에서 갈 수 있는 곳 (정렬된)리스트)
로 저장한다.

bfs는 마찬가지로 큐를 사용해서 방문하면 된다.

프린트를 반복해서 하는 것보다 글로벌변수에 추가한 후 출력할 값들을 저장해 준다.
그렇게 해서 딱 한번만 프린트 호출하면 매번 호출할 때보다 속도가 상당히 개선됨.
'''

def dfs(i):
    r = []
    st = [i]
    while st:
        idx = st.pop()
        if not vl[idx]:
            vl[idx] = 1
            r.append(str(idx))
        for v in range(len(nl[idx])-1, -1, -1):
            if not vl[nl[idx][v]]:
                st.append(nl[idx][v])
    print(' '.join(r))


def bfs(i):
    r = []
    q = deque([i])
    while q:
        idx = q.popleft()
        if not vl[idx]:
            vl[idx] = 1
            r.append(str(idx))
        for v in nl[idx]:
            if not vl[v]:
                q.append(v)
    print(' '.join(r))


N, M, V = map(int, sys.stdin.readline().strip().split())
nl = {i: [] for i in range(1, N+1)}
for m in range(M):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    nl[v1].append(v2)
    nl[v2].append(v1)

for i in range(1, N+1):
    nl[i].sort()
vl = [0 for _ in range(N+1)]
dfs(V)
vl = [0 for _ in range(N+1)]
bfs(V)