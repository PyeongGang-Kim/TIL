import sys
sys.stdin = open('회전.txt')

results = []
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    nl = list(map(int, input().split()))
    results.append('#{} {}'.format(t, nl[M%N]))
print('\n'.join(results))