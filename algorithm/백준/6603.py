import sys
from itertools import combinations
input = sys.stdin.readline

r = []
s = input().strip()
while s != '0':
    nl = list(map(str, s.split()))
    nl.pop(0)
    for i in combinations(nl, 6):
        r.append(' '.join(i))
    r.append('')
    s = input().strip()
print('\n'.join(r))