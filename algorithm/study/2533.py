import sys
sys.setrecursionlimit(1111111)
input = sys.stdin.readline

def gvs(idx, status=0):
    tmp = 0
    if status:
        # 얼리 아답터 뽑아야 함
        tmp = 1
        i = 0
        while i < len(nl[idx]):
            if not vl[nl[idx][i]]:
                if dp[nl[idx][i]][0] != -1:
                    tmp += dp[nl[idx][i]][0]
                else:
                    vl[nl[idx][i]] = True
                    tmp += gvs(nl[idx][i], 0)
                    vl[nl[idx][i]] = False
            i += 1
    else:
        tmp2 = 0
        # 얼리 아답터 안 뽑아도 됨
        # 안 뽑는 경우
        i = 0
        while i < len(nl[idx]):
            if not vl[nl[idx][i]]:
                if dp[nl[idx][i]][1] != -1:
                    tmp += dp[nl[idx][i]][1]
                else:
                    vl[nl[idx][i]] = True
                    tmp += gvs(nl[idx][i], 1)
                    vl[nl[idx][i]] = False
            i += 1
        # 뽑는 경우
        i = 0
        while i < len(nl[idx]):
            if not vl[nl[idx][i]]:
                if dp[nl[idx][i]][0] != -1:
                    tmp2 += dp[nl[idx][i]][0]
                else:
                    vl[nl[idx][i]] = True
                    tmp2 += gvs(nl[idx][i], 0)
                    vl[nl[idx][i]] = False
            i += 1
        tmp = min(tmp, tmp2+1)
    dp[idx][status] = tmp
    return tmp


N = int(input())
nl = [[] for _ in range(N+1)]
dp = [[-1, -1] for _ in range(N+1)]
vl = [False for _ in range(N+1)]
N -= 1
R = 0
while N:
    a, b = map(int, input().split())
    nl[a].append(b)
    nl[b].append(a)
    N -= 1
vl[1] = True
R = gvs(1)
print(R)