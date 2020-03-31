import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    nl = list(map(int, input().split()))
    r = sum(nl)
    print(r if r <= m else m)