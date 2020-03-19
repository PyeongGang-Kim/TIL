import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
nl = [int(input()) for _ in range(N)]
nl = nl + nl
r = 0
cnt = 0
t = k
vl = [0] * (d + 1)
while t:
    t -= 1
    if not vl[nl[t]]:
        cnt += 1
    vl[nl[t]] += 1

if N == k:
    print(cnt)
else:
    t = k
    for i in range(N):
        if not vl[c]:
            r = max(cnt + 1, r)
        else:
            r = max(cnt, r)
        vl[nl[i]] -= 1
        if not vl[nl[i]]:
            cnt -= 1
        if not vl[nl[t]]:
            cnt += 1
        vl[nl[t]] += 1
        t += 1

    print(r)