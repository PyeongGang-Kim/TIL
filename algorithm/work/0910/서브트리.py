import sys
sys.stdin = open('서브트리.txt')


def find(i):
    global cnt
    cnt += 1
    for k in range(E):
        if nl[k*2] == i:
            find(nl[k*2+1])


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    nl = list(map(int, input().split()))
    cnt = 0
    find(N)
    print('#{} {}'.format(t, cnt))