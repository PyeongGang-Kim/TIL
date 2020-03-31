import sys
sys.setrecursionlimit(123470)
input = sys.stdin.readline


def dfs(position):
    if position == 1:
        return 1
    nextPosition = cl[position][1]
    cl[nextPosition][0] += cl[position][0]
    cl[position][0] = 0
    if cl[nextPosition][0] <= 0:
        return nextPosition
    else:
        cl[position][1] = dfs(nextPosition)
        return cl[position][1]


N = int(input())
cl = [[0, 0] for _ in range(N+1)]
for i in range(2, N+1):
    a, b, c = input().split()
    if a == 'S':
        cl[i][0] = int(b)
    else:
        cl[i][0] = -int(b)
    cl[i][1] = int(c)

for i in range(2, N+1):
    if cl[i][0] > 0:
        dfs(i)

print(cl[1][0])