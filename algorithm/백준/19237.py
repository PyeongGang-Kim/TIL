# 각 상어 현재 방향별 우선순위가 존재함

# 상어 정보: 번호, 방향, 위치
# 매 턴마다 죽은 상어가 있었으면 해당 상어를 지워준다.

# 번호순대로 이동 후 냄새를 뿌리면 된다.

# 상어가 살아있는지 확인
# 살아 있으면 이동
# 냄새를 뿌릴 수 있는 곳인지 확인
# 냄새를 뿌릴 수 있으면 뿌린다.
# 뿌릴 수 없으면 상어 사망

# 냄새 뿌리려고 할 때 다른 냄새가 있으면 상어 제거
# 냄새를 저장할 이차원 배열 + 상어를 저장할 배열

td = [0, 2, 3, 1]
D = [[0, -1], [1, 0], [0, 1], [-1, 0]]
N, M, K = map(int, input().split())
# 상어번호, 냄새 사라지는 시간
nl = [[[0, 0] for _ in range(N)] for _ in range(N)]
tl = [list(map(int, input().split())) for _ in range(N)]
shark_dir = list(map(int, input().split()))
shark_priority = [[[td[x-1] for x in map(int, input().split())] for _ in range(4)] for _ in range(M)]
for temp in shark_priority:
    temp[3], temp[2] = temp[2], temp[3]
    temp[2], temp[1] = temp[1], temp[2]
shark_position = [[0, 0] for _ in range(M)]
for j in range(N):
    for i in range(N):
        if tl[j][i]:
            shark_position[tl[j][i]-1] = [i, j]
shark_list = []
for i in range(M):
    # 상어번호, 현재위치, 현재방향, 사망여부
    shark_list.append([i, *shark_position[i], td[shark_dir[i]-1], 0])

turn = 0
while turn < 1001:
    # 각 각 상어 순서대로 수행
    for shark in shark_list:
        # 현재 위치 shark[1], shark[2]
        # 냄새 뿌릴 수 있는지 확인
        if nl[shark[2]][shark[1]][0] == shark[0] or nl[shark[2]][shark[1]][1] <= turn:
            # 뿌릴 수 있으면 냄새 뿌리기
            nl[shark[2]][shark[1]][1] = turn + K
            nl[shark[2]][shark[1]][0] = shark[0]
        else:
            # 뿌릴 수 없으면 사망
            shark[4] = 1
    # 사망한 상어 제거
    shark_list = [shark for shark in shark_list if not shark[4]]
    # 상어 마리 수 세기
    # 1마리이면 종료한다.
    if len(shark_list) == 1:
        break
    #===================== 여기까지가 현재 턴 번호. 이후부터는 새로운 턴이다.
    turn += 1
    for shark in shark_list:
        chk = 1
        # 냄새 없는 곳으로 이동해야 한다. 현재위치 현재 방향에서 우선순위로 진핸
        for tdir in shark_priority[shark[0]][shark[3]]:
            # 확인할 위치
            tx, ty = shark[1] + D[tdir][0], shark[2] + D[tdir][1]
            # 갈 수 있다면?
            if 0 <= tx < N and 0 <= ty < N and nl[ty][tx][1] < turn:
                chk = 0
                shark[1] = tx
                shark[2] = ty
                shark[3] = tdir
                break
            # 냄새 없는곳이 없었다면 자신의 냄새가 있는곳을 확인해 이동한다.
        if chk:
            for tdir in shark_priority[shark[0]][shark[3]]:
                tx, ty = shark[1] + D[tdir][0], shark[2] + D[tdir][1]
                if 0 <= tx < N and 0 <= ty < N and nl[ty][tx][0] == shark[0]:
                    shark[1] = tx
                    shark[2] = ty
                    shark[3] = tdir
                    break
if turn > 1000:
    turn = -1
print(turn)