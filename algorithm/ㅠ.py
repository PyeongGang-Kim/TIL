def dfs(y,x, mymap, trip):
    global ans
    if y<0 or y>=N or x<0 or x>=N:
        ans = max(len(trip), ans)
        return
    flag = True
    for dy, dx in (-1, 0), (1, 0), (0, 1), (0, -1):
        ny = y + dy
        nx = x + dx
        if not (ny<0 or ny>=N or nx<0 or nx>=N):
            if mymap[ny][nx] < trip[-1] and grid_boolen[ny][nx] is False:
                grid_boolen[ny][nx] = True
                dfs(ny, nx, mymap, trip+[mymap[ny][nx]])
                flag = False
                grid_boolen[ny][nx] = False
        else:
            continue
    if flag:
        ans = max(len(trip), ans)
        return

def findmaxplace(val):
    res = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == val:
                res.append([i,j])
    return res
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    grid_boolen = [[False for _ in range(N)] for _ in range(N)]
    maxval = max(map(max, grid))
    maxplace = findmaxplace(maxval)
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(len(maxplace)):
                mycord = maxplace[k]
                if not(mycord[0] == i and mycord[1] == j):
                    grid[i][j] -= K
                    grid_boolen[mycord[0]][mycord[1]] = True
                    dfs(mycord[0], mycord[1], grid, [maxval])
                    grid[i][j] += K
                    grid_boolen[mycord[0]][mycord[1]] = False
    print('#{} {}'.format(tc+1, ans))