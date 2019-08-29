import sys
sys.stdin = open('asdf.txt')


def chk(i, j):
    ni = str(i)
    for k in range(len(ni)):
        if nl[j+k] != ni[k]:
            return False
        if k == len(ni) - 1:
            return True


results = []
T = int(input())
for t in range(1, T+1):
    a, A, b, B = map(int, input().split())
    t1 = a/A
    t2 = b/B
    if t1 > t2:
        results.append('#{} {}'.format(t, 'ALICE'))
    elif t1 == t2:
        results.append('#{} {}'.format(t, 'DRAW'))
    else:
        results.append('#{} {}'.format(t, 'BOB'))

print('\n'.join(results))