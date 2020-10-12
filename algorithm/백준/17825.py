# move 함수는 말이 처음 이동할 때

score_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 26, 27, 28, 22, 24, 30, 35]
move = [
    [0, 1, 2, 3, 4, 5],
    [0, 2, 3, 4, 5, 6],
    [0, 3, 4, 5, 6, 7],
    [0, 4, 5, 6, 7, 8],
    [0, 5, 6, 7, 8, 9],
    [0, 21, 22, 23, 24, 30],
    [0, 7, 8, 9, 10, 11],
    [0, 8, 9, 10, 11, 12],
    [0, 9, 10, 11, 12, 13],
    [0, 10, 11, 12, 13, 14],
    [0, 28, 29, 24, 30, 31],
    [0, 12, 13, 14, 15, 16],
    [0, 13, 14, 15, 16, 17],
    [0, 14, 15, 16, 17, 18],
    [0, 15, 16, 17, 18, 19],
    [0, 27, 26, 25, 24, 30],
    [0, 17, 18, 19, 20, 99],
    [0, 18, 19, 20, 99, 99],
    [0, 19, 20, 99, 99, 99],
    [0, 20, 99, 99, 99, 99],
    [0, 99, 99, 99, 99, 99],
    [0, 22, 23, 24, 30, 31],
    [0, 23, 24, 30, 31, 20],
    [0, 24, 30, 31, 20, 99],
    [0, 30, 31, 20, 99, 99],
    [0, 24, 30, 31, 20, 99],
    [0, 25, 24, 30, 31, 20],
    [0, 26, 25, 24, 30, 31],
    [0, 29, 24, 30, 31, 20],
    [0, 24, 30, 31, 20, 99],
    [0, 31, 20, 99, 99, 99],
    [0, 20, 99, 99, 99, 99],
]

def move_stone(score, dep=1):
    # 종료조건이면
    if dep == 10:
        # 현재 점수를 확인한 후 최대값에 갱신시키고 리턴한다.
        global result
        result = max(score, result)
        return
    for i in range(4):
        # 도착지가 아닌경우 이동시킬지 확인
        if stone[i] < 40:
            # 현재 돌의 위치에서 주사위만큼 이동하는 곳의 좌표
            new_pos = move[stone[i]][nl[dep]]
            # 가게 될 곳이 도착지거나 돌이 없는 곳인 경우에만 이동을 수행함.
            if new_pos == 99 or not index_count[new_pos]:
                # 현재 돌의 위치를 변경시킴
                temp = stone[i]
                index_count[temp] -= 1
                stone[i] = new_pos
                if new_pos < 40:
                    index_count[new_pos] += 1
                    move_stone(score + score_list[new_pos], dep + 1)
                    index_count[new_pos] -= 1
                else:
                    move_stone(score, dep+1)
                stone[i] = temp
                index_count[temp] += 1


nl = list(map(int, input().split()))
result = 0
index_count = [0 for _ in range(32)]
index_count[0] = 3
stone_position = move[0][nl[0]]
index_count[stone_position] = 1
stone = [0, 0, 0, stone_position]
score = score_list[stone_position]

move_stone(score)
print(result)