import sys
'''
s12 + s21 .... 대칭은 항상 더해지므로 맵을 대칭을 합한것으로 더한 후 계산한다.

0 1 2 3 4 5 이렇게 있을 때
0 1 2 와 3 4 5 이런 팀으로 분리하면

인덱스
0에서 1, 0에서 2, 1에서 2의 합
3에서 4, 3에서 5, 4에서 5의 합
둘의 차를 계산하면 된다.

%%%%
r == 0 일때는 탐색을 종료한다.

'''

def solve(dep = 0):
    global r
    if not r:
        return
    if dep == N:
        st = 0
        li = 0
        for i in range(N2-1):
            for j in range(i+1, N2):
                st += nl[start[i]][start[j]]
                li += nl[link[i]][link[j]]
        r = min(r, abs(st-li))
        return
    if len(start) < N2:
        start.append(dep)
        solve(dep+1)
        start.pop()
    if len(link) < N2:
        link.append(dep)
        solve(dep+1)
        link.pop()


N = int(sys.stdin.readline())
N2 = N//2
nl = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r = 40000
for j in range(N-1):
    for i in range(j+1, N):
        nl[j][i] += nl[i][j]

start = []
link = []
solve()
print(r)