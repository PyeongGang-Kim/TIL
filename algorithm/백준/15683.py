'''
각 카메라들 번호에 따라 볼 수 있는 방향들을 정한다.
dr에 각 방향을 볼 때 탐색되는 영역들을 미리 집어넣는다.

카메라 번호 2번일 때의 예시)
2: [[[-1, 0], [1, 0]], [[0, 1], [0, -1]]]
이것은 (좌 우), (상 하) 이렇게 두가지 방법으로 탐색할 수 있다는 의미.

arr에는 각 각의 카메라에 대해서 몇번째 방법으로 탐색할 지 정해놓는 배열이다.
방법이 정해지면 맵을 복사한다.
각 방향에 대해서 탐색을 하면서 복사한 맵을 갱신시켜 준다.
6을 만나거나 맵을 벗어나는 경우 브레이크를 건다.
모두 탐색 한 후 남아있는 0의 갯수를 구하여 결과 r과 비교한다.
r이 더 클 경우 갱신.

모든 방법에 대해서 시도하면 최소 r이 나온다.
'''

def solve(NL, arr=[], dep=0):
    global r
    if dep == NL:
        vl = []
        for i in range(N):
            vl.append(nl[i][:])
        for i, n in enumerate(arr):
            for dx, dy in dr[cams[i][0]][n]:
                k = 1
                while 1:
                    tx, ty = cams[i][1] + dx*k, cams[i][2] + dy*k
                    if 0 <= tx < M and 0 <= ty < N:
                        k += 1
                        if vl[ty][tx] == 6:
                            break
                        else:
                            vl[ty][tx] = 1
                    else:
                        break
        cnt = 0
        for j in range(N):
            for i in range(M):
                if not vl[j][i]:
                    cnt += 1
        r = min(r, cnt)
        return

    for i in range(len(dr[cams[dep][0]])):
        arr.append(i)
        solve(NL, arr, dep+1)
        arr.pop()
        if r == 0:
            return

dr = {
    1: [[[0, 1]], [[0, -1]], [[-1, 0]], [[1, 0]]],
    2: [[[-1, 0], [1, 0]], [[0, 1], [0, -1]]],
    3: [[[0, -1], [1, 0]], [[1, 0], [0, 1]], [[0, 1], [-1, 0]], [[-1, 0], [0, -1]]],
    4: [[[-1, 0], [0, -1], [1, 0]], [[0, -1], [1, 0], [0, 1]], [[1, 0], [0, 1], [-1, 0]], [[0, 1], [-1, 0], [0, -1]]],
    5: [[[0, 1], [0, -1], [-1, 0], [1, 0]]]

}


N, M = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(N)]
cams = []
r = N*M
for j in range(N):
    for i in range(M):
        if nl[j][i]:
            if nl[j][i] == 6:
                pass
            else:
                cams.append([nl[j][i], i, j])
solve(len(cams))
print(r)