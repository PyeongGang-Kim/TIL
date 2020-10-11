def chk_shark(shark, fishes, nl):
    # 현재 위치에서 먹을 수 있는 물고기가 있는지 탐색한다.
    x, y, dir = shark
    cnt = 0
    # 거리 1, 2, 3에 대해서 확인
    for i in range(1, 4):
        dx, dy = D[dir]
        tx, ty = x + dx * i, y + dy * i
        # 격자 안이면
        if 0 <= tx < 4 and 0 <= ty < 4:
            # 먹을 수 있는지 확인
            if nl[ty][tx]:
                # 물고기 지도와 물고기들 다 복사한 후 먹기. 리턴
                new_nl = [[nl[y][x] for x in range(4)] for y in range(4)]
                new_fishes = [fishes[i][:] for i in range(17)]
                new_nl[y][x] = 0
                fish_index = new_nl[ty][tx]
                new_nl[ty][tx] = 99
                new_fishes[fish_index][3] = 0
                new_shark = [tx, ty, new_fishes[fish_index][2]]
                tcnt = fish_index
                cnt = max(cnt, tcnt + move_fish(new_shark, new_fishes, new_nl))
        else:
            break
    return cnt


def move_fish(shark, fishes, nl):
    for fi in range(1, 17):
        if fishes[fi][3]:
            x, y, dir, _ = fishes[fi]
            for i in range(8):
                tx, ty = x + D[(dir + i) % 8][0], y + D[(dir + i) % 8][1]
                if 0 <= tx < 4 and 0 <= ty < 4 and nl[ty][tx] != 99:
                    # 맵 갱신 후에는 물고기 갱신해야한다.
                    fi1 = nl[y][x]
                    fi2 = nl[ty][tx]
                    fishes[fi1][2] = (dir+i)%8
                    # 물고기끼리 교환하는 경우
                    if fi2:
                        fishes[fi1][0], fishes[fi2][0] = fishes[fi2][0], fishes[fi1][0]
                        fishes[fi1][1], fishes[fi2][1] = fishes[fi2][1], fishes[fi1][1]
                    # 그렇지 않은 경우
                    else:
                        fishes[fi1][0] = tx
                        fishes[fi1][1] = ty
                    nl[ty][tx], nl[y][x] = nl[y][x], nl[ty][tx]
                    break
    return chk_shark(shark, fishes, nl)


nl = [[0 for _ in range(4)] for _ in range(4)]
D = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
fishes = [[0, 0, 0, 1] for _ in range(17)]
fish_input = [list(map(int, input().split())) for _ in range(4)]
for j in range(4):
    for i in range(0, 8, 2):
        fish_num = fish_input[j][i]
        dir = fish_input[j][i+1]-1
        fishes[fish_num][0] = i>>1
        fishes[fish_num][1] = j
        fishes[fish_num][2] = dir

for fi in range(1, 17):
    if fishes[fi][3]:
        x = fishes[fi][0]
        y = fishes[fi][1]
        nl[y][x] = fi

# 상어가 0,0 물고기를 먹는다
fi = nl[0][0]
fishes[fi][3] = 0
shark = [0, 0, fishes[fi][2]]
r = nl[0][0]
nl[0][0] = 99
r += move_fish(shark, fishes, nl)
print(r)
