import sys
sys.stdin = open('이진힙.txt')


def enh(i):
    if hp[i] < hp[i//2]:
        hp[i], hp[i//2] = hp[i//2], hp[i]
        enh(i//2)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    hp = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        hp[i] = nl[i-1]
        enh(i)
    r = 0
    while N:
        N //= 2
        r += hp[N]
    print('#{} {}'.format(t, r))