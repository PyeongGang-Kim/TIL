def fndr(x, y, d=4, chk=0):
    if chk:
        return chk

    dl = [0, 0, 0, 0]
    if d != 4:
        dl[d] = 1
    while dl[0] == 0 or dl[1] == 0 or dl[2] == 0 or dl[3] == 0:

        if (maze[y][x + 1] == '0' or maze[y][x + 1] == '3') and dl[0] == 0:
            if maze[y][x + 1] == '3':
                return 1
            dl[0]=1
            maze[y][x + 1] = '1'
            st.append((x, y))
            chk = fndr(x+1, y, 1)
        else:
            dl[0]=1

        if chk:
            return chk

        if (maze[y][x - 1] == '0' or maze[y][x - 1] == '3') and dl[1] == 0:
            if maze[y][x - 1] == '3':
                return 1
            dl[1]=1
            maze[y][x - 1] = '1'
            st.append((x, y))
            chk = fndr(x-1, y, 0)
        else:
            dl[1]=1

        if chk:
            return chk

        if (maze[y + 1][x] == '0' or maze[y + 1][x] == '3') and dl[2] == 0:
            if maze[y + 1][x] == '3':
                return 1
            dl[2]=1
            maze[y + 1][x] = '1'
            st.append((x, y))
            chk = fndr(x, y+1, 3)
        else:
            dl[2]=1

        if chk:
            return chk

        if (maze[y - 1][x] == '0' or maze[y - 1][x] == '3') and dl[3] == 0:
            if maze[y - 1][x] == '3':
                return 1
            dl[3]=1
            maze[y - 1][x] = '1'
            st.append((x, y))
            chk = fndr(x, y-1, 2)
        else:
            dl[3]=1

        if chk:
            return chk

        if len(st):
            st.pop()
        else:
            return chk

    return chk


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    GX = 0
    GY = 0
    SX = 0
    SY = 0
    st = []

    # 미로 초기화 후 벽으로 입력받은 미로 주변을 1로 둘러싼 미로 저장.
    maze = []
    cb = ['1' for i in range(N + 2)]
    maze.append(cb)
    for i in range(N):
        temp = ['1'] + list(input().strip()) + ['1']
        maze.append(temp)
    maze.append(cb)

    # 시작점 SX, SY, 도착점 GX, GY 찾아서 입력
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if maze[y][x] == '3':
                GX, GY = x, y
            elif maze[y][x] == '2':
                SX, SY = x, y

    print('#{} {}'.format(t, fndr(SX, SY)))