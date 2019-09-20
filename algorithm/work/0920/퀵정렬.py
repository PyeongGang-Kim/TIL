import sys
sys.stdin = open('퀵정렬.txt')


def qs(l, r):
    if l >= r:
        return
    left = l
    right = r
    p = l
    P = A[l]
    while l < r:
        while P < A[r]:
            r -= 1
        while l < r and P >= A[l]:
            l += 1
        A[l], A[r] = A[r], A[l]
    A[p] = A[l]
    A[l] = P
    qs(left, l-1)
    qs(l+1, right)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    qs(0, len(A)-1)
    print('#{} {}'.format(t, A[N//2]))