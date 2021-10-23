import sys
input = sys.stdin.readline

# 각 사람마다 좋아하는 사람 네명 저장할 배열 필요
# 배치할 때 행 열 순으로 반복문 구성. 가장 높은 수 나올때 초기화 같은 수 나올때 무시
# 빈 칸 중 좋아하는 사람 많은 곳으로 구성
# 같은곳이 존재할 경우 빈 칸이 많은 곳으로 배치
# 빈칸도 같은경우 먼저 갱신된 곳으로 배치.


# 비어있는 맵 차례로 채워가면서 확인한다.
D = [[0, 1], [0, -1], [-1, 0], [1, 0]]
def find_and_set(num):
    # 좋아하는 맥스값
    # 비어있는 맥스값
    # 가장 좋은 좌표
    g_max = -1
    n_max = -1

    gx, gy = 0, 0

    for j in ran:
        for i in ran:
            if nl[j][i]:
                continue
            tgcnt = 0
            ngcnt = 0
            for dx, dy in D:
                tx, ty = i + dx, j + dy
                if 0 <= tx < N and 0 <= ty < N:
                    # 값이 있다면 이미 배치된 사람이 있는 것.
                    if nl[ty][tx]:
                        # 배치된 사람이 좋은 사람일 경우
                        if nl[ty][tx] in gl[num]:
                            tgcnt += 1
                    # 비어있는 칸일 경우
                    else:
                        ngcnt += 1
            # 네방향 다 돌아봤으면 최대값 갱신했는지 확인해야한다.
            # 좋은친구수를 갱신했으면 좌표 초기화.
            if tgcnt > g_max:
                gx, gy = i, j
                n_max = ngcnt
                g_max = tgcnt
            # 좋은친구 수가 같다면
            elif tgcnt == g_max:
                # 빈칸 갯수 비교해서 빈칸이 더 많다면 현재 위치로 갱신
                if ngcnt > n_max:
                    gx, gy = i, j
                    n_max = ngcnt
    # 모든 칸 탐색 종료. 배치한다.
    nl[gy][gx] = num

def cal_score():
    total_score = 0
    for j in ran:
        for i in ran:
            tmp_score = 0
            for dx, dy in D:
                tx, ty = i + dx, j + dy

                if 0 <= tx < N and 0 <= ty < N:
                    if nl[ty][tx] in gl[nl[j][i]]:
                        if tmp_score:
                            tmp_score *= 10
                        else:
                            tmp_score += 1
            total_score += tmp_score
    return total_score



N = int(input())
ran = range(N)
nl = [[0 for _ in ran] for _ in ran]
gl = [[] for _ in range(N*N+1)]
sl = []
for _ in range(N*N):
    n, x1, x2, x3, x4 = map(int, input().split())
    gl[n] = [x1, x2, x3, x4]
    sl.append(n)

for num in sl:
    find_and_set(num)
print(cal_score())