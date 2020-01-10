import sys
input = sys.stdin.readline
N, M = map(int, input().split())
T = int(input())
nl1 = [False for _ in range(N+1)]
nl2 = [False for _ in range(M+1)]
while T:
    T -= 1
    a, b = map(int, input().split())
    if a:
        nl1[b] = True
    else:
        nl2[b] = True
cnt1 = 0
cnt2 = 0
idx = 1
maxcnt1 = 0
maxcnt2 = 0
while idx < N+1:
    cnt1 += 1
    maxcnt1 = max(maxcnt1, cnt1)
    if nl1[idx]:
        cnt1 = 0
    idx += 1
idx = 1
while idx < M+1:
    cnt2 += 1
    maxcnt2 = max(maxcnt2, cnt2)
    if nl2[idx]:
        cnt2 = 0
    maxcnt2 = max(maxcnt2, cnt2)
    idx += 1
print(maxcnt1*maxcnt2)