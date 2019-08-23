import time
import sys
sys.stdin = open('asdf.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = set(input().split())
    ml = input().split()
    cnt = 0
    for n in nl:
        for m in ml:
            nl-{m}
    result = N - len(nl)
    print('#{} {}'.format(t, result))