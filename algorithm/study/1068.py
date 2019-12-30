'''
루트 노드도 지울 수 있다.
'''

N = int(input())
nl = list(map(int, input().split()))
ccnt = [0 for _ in range(N)]
for i in range(N):
    if nl[i] == -1:
        start = i
    else:
        ccnt[nl[i]] += 1


tmp = int(input())
if tmp == start:
    print(0)
else:
    ccnt[nl[tmp]] -= 1
    nl[tmp] = -1
    cnt = 0
    for i in range(N):
        if not ccnt[i]:
            tmp = i
            while nl[tmp] != -1:
                tmp = nl[tmp]
            if tmp == start:
                cnt += 1
    print(cnt)