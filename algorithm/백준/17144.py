import sys
'''
R 행 갯수, C열 갯수, T시간

공기청정기 좌표를 저장한다.

미세먼지를 확산하는 로직
빈 공간으로 퍼져나갈 수 있다.
현재 먼지량의 1//5만큼씩 퍼져나간다.
따로 저장해 놓는다.

공기청정기 좌표 두 개에 대해서 먼지를 돌리는 로직 구한다.

%%
더 이상 미세먼지가 분산할 수 없는 경우엔(5 미만으로 내려가는 것들 카운팅)
공기청정기가 제거할 수 있는 먼지를 다 제거한 후 끝내면 된다.
'''
#
# sys.stdin = open('asdf.txt')
R, C, T = map(int, sys.stdin.readline().split())
ml = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
t = 0
for j in range(R):
    if ml[j][0] == -1:
        p1 = j
        p2 = j+1
        break
total_dust = 2
for j in range(R):
    for i in range(C):
        total_dust += ml[j][i]


while total_dust and t < T:
    t += 1
    tmp = [[0 for _ in range(C)] for _ in range(R)]
    for j in range(R):
        for i in range(C):
            if ml[j][i] > 4:
                d_dust = ml[j][i] // 5
                tcnt = 0
                for dx, dy in d:
                    tx, ty = i + dx, j + dy
                    if 0 <= tx < C and 0 <= ty < R and ml[ty][tx] != -1:
                        tcnt += 1
                        tmp[ty][tx] += d_dust
                ml[j][i] -= tcnt*d_dust
    for j in range(R):
        for i in range(C):
            ml[j][i] += tmp[j][i]


    total_dust -= ml[p1-1][0] + ml[p2+1][0]
    for j in range(p1-1, 0, -1):
        g = ml[j-1][0]
        ml[j][0] = g
    for i in range(C-1):
        g = ml[0][i+1]
        ml[0][i] = g
    for j in range(p1):
        g = ml[j+1][C-1]
        ml[j][C-1] = g
    for i in range(C-1, 1, -1):
        g = ml[p1][i-1]
        ml[p1][i] = g
    for j in range(p2+1, R-1):
        g = ml[j+1][0]
        ml[j][0] = g
    for i in range(C-1):
        g = ml[R-1][i+1]
        ml[R-1][i] = g
    for j in range(R-1, p2, -1):
        g = ml[j-1][C-1]
        ml[j][C-1] = g
    for i in range(C-1, 1, -1):
        g = ml[p2][i-1]
        ml[p2][i] = g
    ml[p1][1] = 0
    ml[p2][1] = 0

print(total_dust)