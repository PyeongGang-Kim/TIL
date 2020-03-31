'''
거쳐가는 경로가 있을 경우 현재 경로룰 없애도 된다(무한대)
거쳐가는 경로가 더 작은경우 말이 안되는 경우이다(-1)
그 외의 경우는 꼭 필요한 도로이다.
'''
def floid():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j and i != k and k != j:
                    if nl[i][j] != inf and nl[i][j] > nl[i][k] + nl[k][j]:
                        return -1
                    elif nl[i][j] == nl[i][k] + nl[k][j]:
                            nl[i][j] = inf
    r = 0
    for j in range(N):
        for i in range(j+1, N):
            if nl[j][i] != inf:
                r += nl[j][i]
    return r


inf = 0xfffffff
N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]
print(floid())