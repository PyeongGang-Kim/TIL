import sys
sys.stdin = open('이진탐색.txt')


def mid(i = 1):
    global cnt
    if i*2 <=N:
        mid(i*2)
    tree[i] = cnt
    cnt += 1
    if i*2 +1<= N:
        mid(i*2+1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0 for i in range(N+1)]
    cnt = 1
    mid()
    print('#{} {} {}'.format(t, tree[1], tree[N//2]))