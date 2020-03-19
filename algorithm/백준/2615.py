def detect(x, y):
    if (x-1 >= 0 and nl[y][x] != nl[y][x-1]) or x == 0:
        cnt = 1
        tx = x
        while True:
            tx += 1
            if tx < 19 and nl[y][tx] == nl[y][x]:
                cnt += 1
            else:
                break
        if cnt == 5:
            return True

    if (x-1 >= 0 and y-1>=0 and nl[y][x] != nl[y-1][x-1]) or (x==0 or y==0):
        cnt = 1
        tx = x
        ty = y
        while True:
            tx += 1
            ty += 1
            if tx < 19 and ty < 19 and nl[ty][tx] == nl[y][x]:
                cnt += 1
            else:
                break
        if cnt == 5:
            return True
    if (x - 1 >= 0 and y + 1 < 19 and nl[y][x] != nl[y + 1][x - 1]) or x == 0 or y == 18:
        cnt = 1
        tx = x
        ty = y
        while True:
            tx += 1
            ty -= 1
            if tx < 19 and ty >= 0 and nl[ty][tx] == nl[y][x]:
                cnt += 1
            else:
                break
        if cnt == 5:
            return True

    if (y-1 >= 0 and nl[y][x] != nl[y-1][x]) or y == 0:
        cnt = 1
        ty = y
        while True:
            ty += 1
            if ty < 19 and nl[ty][x] == nl[y][x]:
                cnt += 1
            else:
                break
        if cnt == 5:
            return True
    return False

nl = [list(map(int, input().split())) for _ in range(19)]
chk = False
for j in range(19):
    if chk:
        break
    for i in range(19):
        if nl[j][i]:
            if detect(i, j):
                print(nl[j][i])
                print(j+1, i+1)
                chk = True
                break
if not chk:
    print(0)