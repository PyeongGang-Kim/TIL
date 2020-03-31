import sys
input = sys.stdin.readline
from collections import deque

def mergecnt(s, e):
    global cnt
    if s == e:
        return deque([nl[s]])
    if s+1 == e:
        if nl[s] > nl[e]:
            cnt += 2
            return deque([nl[e], nl[s]])
        else:
            return deque([nl[s], nl[e]])
    m = (s+e)//2
    l1 = mergecnt(s, m)
    l2 = mergecnt(m+1, e)
    i = s
    i1 = s
    i2 = m+1
    tim = e+1
    l = deque()
    while i < tim:
        if l1 and l2:
            if l1[0] <= l2[0]:
                l.append(l1.popleft())
                cnt += abs(i - i1)
                i1 += 1
                i += 1
            else:
                l.append(l2.popleft())
                cnt += abs(i - i2)
                i2 += 1
                i += 1
        elif l1:
            l.append(l1.popleft())
            cnt += abs(i - i1)
            i1 += 1
            i += 1
        else:
            l.append(l2.popleft())
            cnt += abs(i - i2)
            i2 += 1
            i += 1
    return l

N = int(input())
nl = list(map(int, input().split()))
cnt = 0
mergecnt(0, N-1)
print(cnt//2)