import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def qsort(s, e, nl):
    if s >= e:
        return

    # 피봇을 고르고 나서 피봇보다 작은 것들만 왼쪽에
    # 큰것들만 오른쪽에 남겨야 한다.

    piv = nl[s]

    i = s
    j = e
    while i <= j:
        while i < e and nl[i] <= piv:
            i += 1

        while nl[j] >= piv and j >= i:
            j -= 1

        if j <= i:
            # j위치가 피봇의 위치로 적절하다.
            nl[j], nl[s] = nl[s], nl[j]
            break
        else:
            nl[j], nl[i] = nl[i], nl[j]


    qsort(s, j-1, nl)
    qsort(j+1, e, nl)




N = int(input())

nl = [int(input()) for _ in range(N)]
qsort(0, len(nl)-1, nl)
r = [str(x) for x in nl]
print('\n'.join(r))