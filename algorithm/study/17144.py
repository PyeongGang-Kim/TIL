import sys
'''
R 행 갯수, C열 갯수, T시간

공기청정기 좌표를 저장한다.

미세먼지를 확산하는 로직
빈 공간으로 퍼져나갈 수 있다.
현재 먼지량의 1//5만큼씩 퍼져나간다.
따로 저장해 놓는다.

공기청정기 좌표 두 개에 대해서 먼지를 돌리는 로직 구한다.

'''
sys.stdin = open('asdf.txt')
R, C, T = map(int, sys.stdin.readline().split())
ml = {}
p = []
for j in range(R):
    tmp = map(int, sys.stdin.readline().split())
    i = 0
    for n in tmp:
        if n:
            if n != -1:
                ml[(i, j)] = n
            else:
                p.append(j)
        i += 1
p1 = p[0]
p2 = p[1]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
t = 0
while t < T:
    t += 1
    tmp = {}
    for P, v in ml:
        d_dust = v // 5
        tcnt = 0
        for dx, dy in d:
            tx, ty = P[0] + dx, P[1] + dy
            if 0 <= tx < C and 0 <= ty < R and (tx == 0 and (ty != p1 and ty != p2)):
                tcnt += 1
                if tmp.get((tx, ty)):
                    tmp[(tx, ty)] += d_dust
                else:
                    tmp[(tx, ty)] = d_dust
        ml[P] -= tcnt*d_dust

    for P, v in tmp.items():
        if ml.get(P):
            ml[P] += v
        else:
            ml[P] = v

    del ml[(0, p1-1)]
    del ml[(0, p2+1)]
    for j in range(p1-2, -1, -1):
        tmp = ml.get((0, j))
        if tmp:
            ml[(0, j-1)] = tmp
            del ml[(0, j)]
    for i in range(1, C):
        tmp = ml.get((i, 0))
        if tmp:
            ml[(i-1, 0)] = tmp
            del ml[(i, 0)]
    for j in range(1, p1+1):
        tmp = ml.get((C-1, j))
        if tmp:
            ml[(C-1, j-1)] = tmp
            del ml[(C-1, j)]
    for i in range(C-2, 0, -1):
        tmp = ml.get((i, p1))
        if tmp:
            ml[(i+1, p1)] = tmp
            del ml[(i, p1)]

    for j in range(p2+1, R-1):
        ml[j][0], ml[j+1][0] = ml[j+1][0], ml[j][0]
    for i in range(C-1):
        ml[R-1][i], ml[R-1][i+1] = ml[R-1][i+1], ml[R-1][i]
    for j in range(R-1, p2, -1):
        ml[j][C-1], ml[j-1][C-1] = ml[j-1][C-1], ml[j][C-1]
    for i in range(C-1, 1, -1):
        ml[p2][i], ml[p2][i-1] = ml[p2][i-1], ml[p2][i]

r = 0
for j in range(R):
    for i in range(C):
        if ml[j][i] and ml[j][i] != -1:
            r += ml[j][i]
print(r)