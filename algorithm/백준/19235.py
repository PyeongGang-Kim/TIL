gl = [[0 for _ in range(6)] for _ in range(4)]
bl = [[0 for _ in range(4)] for _ in range(6)]

bn = 1
score = 0

def set_green(t, x, y, bn):
    global gl
    # 블록 타입 각 각에 대해서 현 위치 비워줄 것
    if t == 1:
        if x != 5:
            gl[y][x] = 0
            for i in range(x, 5):
                if gl[y][i+1]:
                    gl[y][i] = bn
                    break
                if i == 4:
                    gl[y][5] = bn
    elif t == 2:
        if x != 5:
            gl[y][x] = 0
            gl[y+1][x] = 0
            for i in range(x, 5):
                if gl[y][i+1] or gl[y+1][i+1]:
                    gl[y][i] = bn
                    gl[y+1][i] = bn
                    break
                if i == 4:
                    gl[y][5] = bn
                    gl[y+1][5] = bn
    else:
        if x != 4:
            gl[y][x] = 0
            gl[y][x+1] = 0
            for i in range(x, 4):
                if gl[y][i+2]:
                    gl[y][i] = bn
                    gl[y][i+1] = bn
                    break
                if i == 3:
                    gl[y][5] = bn
                    gl[y][4] = bn

def check_green():
    """
    블록 배치 후 라인클리어 가능한지 확인
    라인 클리어 가능하면 점수 얻고 라인 지워준다.
    점수 얻었으면 True, 아니면 False 반환한다.
    """
    global score
    result = False
    for i in range(5, 1, -1):
        chk = True
        for j in range(4):
            if not gl[j][i]:
                chk = False
                break
        if chk:
            for j in range(4):
                gl[j][i] = 0
            score += 1
            result = True
    return result


def rearrange_green():
    """
    블록이 터진 후 재배치를 위한 모듈
    """
    for i in range(5, -1, -1):
        for j in range(4):
            if gl[j][i]:
                # 네 방향 확인
                chk = False
                chk_d = False
                chk_r = False
                if 0 < i and gl[j][i] == gl[j][i-1]:
                    chk = True
                if i < 5 and gl[j][i] == gl[j][i+1]:
                    chk = True
                    chk_r = True
                if 0 < j and gl[j][i] == gl[j-1][i]:
                    chk = True
                if j < 3 and gl[j][i] == gl[j+1][i]:
                    chk = True
                    chk_d = True
                # 아무것도 체크 안됐으면 1칸
                if not chk:
                    set_green(1, i, j, gl[j][i])
                # 아래쪽이 체크됐으면
                elif chk_d:
                    set_green(2, i, j, gl[j][i])
                # 오른쪽이 체크됐으면
                elif chk_r:
                    set_green(3, i, j, gl[j][i])

def push_green(n):
    for i in range(6-n, 6):
        for j in range(4):
            gl[j][i] = 0
    for i in range(5, n-1, -1):
        for j in range(4):
            gl[j][i] = gl[j][i-n]
    for i in range(n):
        for j in range(4):
            gl[j][i] = 0

def check_green2():
    for i in range(2):
        for j in range(4):
            if gl[j][i]:
                if i:
                    push_green(1)
                    return
                push_green(2)
                return


def set_blue(t, x, y, bn):
    global bl
    # 블록 타입 각 각에 대해서 현 위치 비워줄 것
    if t == 1:
        if y != 5:
            bl[y][x] = 0
            for j in range(y, 5):
                if bl[j+1][x]:
                    bl[j][x] = bn
                    break
                if j == 4:
                    bl[5][x] = bn
    elif t == 2:
        if y != 4:
            bl[y][x] = 0
            bl[y+1][x] = 0
            for j in range(y, 4):
                if bl[j+2][x]:
                    bl[j][x] = bn
                    bl[j+1][x] = bn
                    break
                if j == 3:
                    bl[5][x] = bn
                    bl[4][x] = bn
    else:
        if y != 5:
            bl[y][x] = 0
            bl[y][x+1] = 0
            for j in range(y, 5):
                if bl[j+1][x] or bl[j+1][x+1]:
                    bl[j][x] = bn
                    bl[j][x+1] = bn
                    break
                if j == 4:
                    bl[5][x] = bn
                    bl[5][x+1] = bn

def check_blue():
    """
    블록 배치 후 라인클리어 가능한지 확인
    라인 클리어 가능하면 점수 얻고 라인 지워준다.
    점수 얻었으면 True, 아니면 False 반환한다.
    """
    global score
    result = False
    for j in range(5, 1, -1):
        chk = True
        for i in range(4):
            if not bl[j][i]:
                chk = False
                break
        if chk:
            for i in range(4):
                bl[j][i] = 0
            score += 1
            result = True
    return result


def rearrange_blue():
    """
    블록이 터진 후 재배치를 위한 모듈
    """
    for j in range(5, -1, -1):
        for i in range(4):
            if bl[j][i]:
                # 네 방향 확인
                chk = False
                chk_d = False
                chk_r = False
                if 0 < i and bl[j][i] == bl[j][i-1]:
                    chk = True
                if i < 3 and bl[j][i] == bl[j][i+1]:
                    chk = True
                    chk_r = True
                if 0 < j and bl[j][i] == bl[j-1][i]:
                    chk = True
                if j < 5 and bl[j][i] == bl[j+1][i]:
                    chk = True
                    chk_d = True
                # 아무것도 체크 안됐으면 1칸
                if not chk:
                    set_blue(1, i, j, bl[j][i])
                # 아래쪽이 체크됐으면
                elif chk_d:
                    set_blue(2, i, j, bl[j][i])
                # 오른쪽이 체크됐으면
                elif chk_r:
                    set_blue(3, i, j, bl[j][i])

def push_blue(n):
    for j in range(6-n, 6):
        for i in range(4):
            bl[j][i] = 0
    for j in range(5, n-1, -1):
        for i in range(4):
            bl[j][i] = bl[j-n][i]
    for j in range(n):
        for i in range(4):
            bl[j][i] = 0

def check_blue2():
    for j in range(2):
        for i in range(4):
            if bl[j][i]:
                if j:
                    push_blue(1)
                    return
                push_blue(2)
                return

N = int(input())
for n in range(N):
    t, x, y = map(int, input().split())
    set_green(t, 0, y, bn)
    while check_green():
        rearrange_green()
    check_green2()
    set_blue(t, x, 0, bn)
    while check_blue():
        rearrange_blue()
    check_blue2()
    bn += 1
print(score)
cnt = 0
for i in range(4):
    for j in range(2, 6):
        if bl[j][i]:
            cnt += 1
for i in range(2, 6):
    for j in range(4):
        if gl[j][i]:
            cnt += 1
print(cnt)