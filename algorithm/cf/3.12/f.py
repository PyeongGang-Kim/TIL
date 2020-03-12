import sys
input = sys.stdin.readline


def dfs(i):
    #cnt1 최소값, cnt2 최대값
    cnt1, cnt2 = 0, 0
    # 메모이제이션. 내가 현재 갈 수 있는 모든 간선을 검색
    for edge in ml[i]:
        if not vl[edge[0]]:
            #갈 수 있는 간선이다. 간선 값이 있는지 확인
            if not (edge[1] or edge[2]):
                #간선 값이 없으면 dfs 수행
                vl[edge[0]] = 1
                edge[1], edge[2] = dfs(edge[0])
                vl[edge[0]] = 0
            cnt1 += edge[1]
            cnt2 += edge[2]

    # 내가 흰색인 경우
    if nl[i]:
        cnt1 += 1
        if cnt1 == 1:
            cnt1 = 0
        cnt2 += 1
    else:
        #검은색
        cnt1 -= 1
        cnt2 -= 1
        if cnt2 == -1:
            cnt2 = 0
    return cnt1, cnt2


n = int(input())
nl = [0] + list(map(int, input().split()))
k = n - 1

ml = [[] for _ in range(n+1)]
while k:
    k -= 1
    a, b = map(int, input().split())
    ml[a].append([b, 0, 0])
    ml[b].append([a, 0, 0])

vl = [0] * (n+1)
r = []
for i in range(1, n+1):
    vl[i] = 1
    t1, t2 = dfs(i)
    vl[i] = 0
    r.append(str(max(abs(t1), t2)))
print('\n'.join(r))