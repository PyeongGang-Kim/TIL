import sys
sys.stdin = open('토너먼트카드게임_input.txt')


def ST(i, j):
    if i == j:
        return nl[i], i
    t1, i1 = ST(i, (i+j)//2)
    t2, i2 = ST((i+j)//2+1, j)
    if r[t1-1] == r[t2-2]:
        return t2, i2
    else:
        return t1, i1


results =[]
r = [1, 2, 3]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    c, i = ST(0, len(nl)-1)
    results.append('#{} {}'.format(t, i+1))
print('\n'.join(results))
