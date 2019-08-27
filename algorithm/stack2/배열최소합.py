import sys
sys.stdin = open('배열최소합_input.txt')


def dfsp(d=0, s = 0):
    global result
    if d == N:
        if not result:
            result = s
        elif result > s:
            result = s
    if s > result and result:
        return
    for i in range(N):
        if not vl[i]:
            arr.append(i)
            vl[i] = 1
            dfsp(d+1, s+nl[d][i])
            arr.pop()
            vl[i] = 0


results = []
T = int(input())
for t in range(1, T+1):
    cnt = 0
    N = int(input())
    nl = [list(map(int, input().split())) for _ in range(N)]
    vl = [0]*N
    arr = []
    result = 0
    dfsp()
    results.append('#{} {}'.format(t, result))
print('\n'.join(results))