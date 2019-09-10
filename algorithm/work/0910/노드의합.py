import sys
sys.stdin = open('노드의합.txt')


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    nl = [0 for _ in range(N+1)]
    for m in range(M):
        t1, t2 = map(int, input().split())
        nl[t1] = t2
    for i in range(N, 1, -1):
        nl[i//2] += nl[i]
    print('#{} {}'.format(t, nl[L]))