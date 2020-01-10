import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def gvs(idx, status=0):
    tmp = 0
    if status:
        # 뽑으면 안됨
        for i in nl2[idx]:
            if not vl[i]:
                if dp[i][0]:
                    tmp += dp[i][0]
                else:
                    vl[i] = True
                    tmp += gvs(i, 0)
                    vl[i] = False
    else:
        # 뽑아도 되고 안뽑아도 됨
        tmp2 = 0
        for i in nl2[idx]:
            if not vl[i]:
                if dp[i][0]:
                    tmp += dp[i][0]
                else:
                    vl[i] = True
                    tmp += gvs(i, 0)
                    vl[i] = False
                if dp[i][1]:
                    tmp2 += dp[i][1]
                else:
                    vl[i] = True
                    tmp2 += gvs(i, 1)
                    vl[i] = False
        tmp = max(tmp, tmp2+nl[idx])
    dp[idx][status] = tmp
    return tmp


N = int(input())
nl = [0] + list(map(int, input().split()))
nl2 = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
vl = [False for _ in range(N+1)]
N2 = N
N -= 1
R = 0
while N:
    a, b = map(int, input().split())
    nl2[a].append(b)
    nl2[b].append(a)
    N -= 1
vl[1] = True
R = gvs(1)
print(R)