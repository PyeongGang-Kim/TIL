import sys
sys.stdin = open('노드의거리.txt')


def bfs():
    Q = [[S, 0]]
    while Q:
        k, d = Q.pop(0)
        for n in nl:
            if n[0] == k and not vl[n[1]]:
                if n[1] == G:
                    return d+1
                Q.append([n[1], d+1])
                vl[n[1]] = 1
            elif n[1] == k and not vl[n[0]]:
                if n[0] == G:
                    return d+1
                Q.append([n[0], d+1])
                vl[n[0]] = 1

    return 0


results = []
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    vl = [0 for _ in range(V+1)]
    vl[S] = 1
    results.append('#{} {}'.format(t, bfs()))
print('\n'.join(results))