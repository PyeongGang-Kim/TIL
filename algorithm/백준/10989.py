import sys
input = sys.stdin.readline
N = int(input())
nl = [0 for _ in range(10001)]
i = 0
while i < N:
    i += 1
    nl[int(input())] += 1

r = []
i = 1
while i < 10001:
    j = 0
    while j < nl[i]:
        print(i)
        j += 1
    i += 1
