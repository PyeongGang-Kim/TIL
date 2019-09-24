import sys
sys.stdin = open('3064.txt')
'''
내가 인풋으로 받는 리스트 갯수보다 크거나 같은 단말노드를 가지는 완전 이진트리를 만든다.
재귀식을 통해 루트에서부터 자식의 합을 구한다. 현재 깊이가 랭크(dep)가 초과하면 단말노드이므로 해당하는 값을 리턴한다.
부모 노드에 자식 노드의 합을 입력해준다.

구간합이 입력된 완전이진트리를 만들었다.

구간합을 분할정복을 통해 구한다.

분할한 구간이 내가 구하고자 하는 구간합 범위 안에 속하면 해당 값을 리턴한다.
분할한 구간이 아예 벗어날 경우 0을 리턴한다.
그 이외의 경우 구간을 다시 분할한다.

'''
def mkl(idx = 1, d = 1):
    if d > dep:
        return a[idx]
    a[idx] = mkl(idx*2, d+1) + mkl(idx*2+1, d+1)
    return a[idx]


def add(idx, nn):
    i = n + idx - 1
    a[i] += nn
    i //= 2
    while i:
        a[i] = a[i*2] + a[i*2 + 1]
        i //= 2


def sumlr(s, e, i = 1):
    if e < l or s > r:
        return 0
    if l <= s and e <= r:
        return a[i]
    m = (s+e)//2
    return sumlr(s, m, i*2) + sumlr(m+1, e, i*2+1)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    results = ['#%d' %t]
    nl = list(map(int, input().split()))
    n = 1
    dep = 0
    while n < N:
        n *= 2
        dep += 1

    a = [0 for _ in range(2*n+1)]
    for i in range(N):
        a[n+i] = nl[i]

    mkl()
    for m in range(M):
        o, l, r = map(int, input().split())
        if o == 1:
            add(l, r)
        else:
            num = sumlr(1, n)
            results.append(str(num))
    print(' '.join(results))