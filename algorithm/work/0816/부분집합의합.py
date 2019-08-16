import sys
sys.stdin = open('부분집합의합_input.txt')


def subset(c, i=1, d=0, arr=[]):
    global cnt
    if d == N:
        if sum(arr) == K:
            cnt += 1
            arr.pop()
            return
    if i>12:
        if c:
            arr.pop()
        return
    else:
        subset(0, i+1, d, arr)
        arr.append(i)
        subset(1, i+1, d+1, arr)
    if c:
        arr.pop()


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    subset(0)
    print('#{} {}'.format(t, cnt))