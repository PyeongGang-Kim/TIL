import time
import sys
sys.stdin = open('asdf.txt')


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = set(input().split())
    ml = set(input().split())
    print('#{} {}'.format(t, len(nl&ml)))