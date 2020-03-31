import sys
input = sys.stdin.readline
N = int(input())
nl = [int(input()) for _ in range(N)]
nl.sort()
print('\n'.join(map(str, nl)))