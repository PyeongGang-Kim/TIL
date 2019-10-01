from collections import deque
'''
같은 루트노드를 가지게 될 경우가 사이클이 생길 수 있는 좌표이다.
그 좌표들을 모아놓고 bfs를 하면서 원점을 만나면 그게 최단 사이클의 거리이다.

'''
def unionfind(i):
    if cl[i]:
        tmp = unionfind(cl[i])
        cl[i] = tmp
        return tmp
    return i


def bfs(i):
    Q = deque([[0, i]])
    vl = [False for _ in range(N+1)]
    vl[i] = True
    while Q:
        d, idx = Q.popleft()
        if ml[idx]:
            for k in ml[idx]:
                if vl[k]:
                    if k == i:
                        return d+1
                else:
                    vl[k] = True
                    Q.append([d+1, k])


T = int(input())
for t in range(1, T+1):

    nod = set()
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    ml = {i: [] for i in range(1, N+1)}

    cl = [0 for _ in range(N+1)]
    for a, b in nl:
        ml[a].append(b)
        r1, r2 = unionfind(a), unionfind(b)
        if r1 == r2:
            nod.add(a)
            nod.add(b)
        else:
            cl[r1] = r2
    R = 0xffffffff
    for idx in nod:
        R = min(R, bfs(idx))
    print('#{} {}'.format(t, R))