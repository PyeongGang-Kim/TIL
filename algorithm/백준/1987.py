def dfs(i, j, cnt=1):
    global result
    if result < cnt:
        result = cnt
    for k in range(4):
        i_tem = i + dx[k]
        j_tem = j + dy[k]
        if 0 <= i_tem < R and 0 <= j_tem < C and not vl[nl[i_tem][j_tem]]:
                vl[nl[i_tem][j_tem]] = True
                dfs(i_tem, j_tem, cnt + 1)
                vl[nl[i_tem][j_tem]] = False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
nl = [[ord(a)-65 for a in list(input())] for j in range(R)]
vl = [False for _ in range(26)]
result = 0
vl[nl[0][0]] = True
dfs(0, 0)
print(result)