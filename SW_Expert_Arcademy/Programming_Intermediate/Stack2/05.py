# def fndr(x,y):


T=int(input())
for t in range(1,T+1):
    N=int(input())
    GX=0
    GY=0
    SX=0
    SY=0
    st=[]

    #미로 초기화 후 벽으로 입력받은 미로 주변을 1로 둘러싼 미로 저장.
    maze=[]
    cb=['1' for i in range(N+2)]
    maze.append(cb)
    for i in range(N):
        temp=['1']+list(input().strip())+['1']
        maze.append(temp)
    maze.append(cb)

    #시작점 SX, SY, 도착점 GX, GY 찾아서 입력
    for y in range(1,N+1):
        for x in range(1,N+1):
            if maze[y][x]=='3':
                GX, GY = x, y
            elif maze[y][x]=='2':
                SX, SY = x, y

