import time
import sys
sys.stdin = open('asdf.txt')

results = []
T = int(input())
for t in range(1, T+1):
    N = input()
    while len(N)>1:
        tmp = 0
        for n in N:
            tmp += int(n)
        N = str(tmp)
    if t == 10:
        results.append('#{} {}'.format(t, '-10'))
    else:
        results.append('#{} {}'.format(t, N))
print('\n'.join(results))
