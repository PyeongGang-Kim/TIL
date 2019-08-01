class Node:
    def __init__(self, item, cnt=0, n=None):
        self.item = item
        self.next = n
        self.cnt = cnt
        maze[self.item[1]][self.item[0]]=1


def enQ(inNode):
    global front, rear
    if not front:
        front = inNode
    else:
        rear.next = inNode
    rear = inNode


def deQ():
    global front, rear
    tmp=front.cnt
    maze[front.item[1]][front.item[0]]=1
    if front.next is None:
        front, rear = None, None
        return tmp
    front=front.next
    return tmp


T=int(input())
for t in range(1,T+1):
    N = int(input())
    maze = []
    cb = [1 for i in range(N + 2)]
    maze.append(cb)
    for i in range(N):
        temp = [1] + list(map(int, input().strip())) + [1]
        maze.append(temp)
    maze.append(cb)
    gx, gy, sx, sy, chk, tmp = 0, 0, 0, 0, 0, 0
    for y in range(1, N + 1):
        if chk == 2:
            break
        for x in range(1, N + 1):
            if maze[y][x] == 3:
                gx, gy = x, y
                chk +=1
            if maze[y][x] == 2:
                sx, sy = x, y
                chk += 1

    front, rear = None, None
    enQ(Node((sx,sy)))
    cnt=0
    while front is not None:
        if front:
            x=front.item[0]
            y=front.item[1]
            maze[y][x]=1
        else:
            break
        #d 1은 오른쪽금지 2는 왼쪽금지 3은 위쪽금지 4는 아래쪽금지
        if maze[y][x + 1]!=1:
            if maze[y][x + 1] == 3:
                break
            enQ(Node((x + 1,y), front.cnt + 1))

        if maze[y][x - 1]!=1:
            if maze[y][x - 1] == 3:
                break
            enQ(Node((x-1, y), front.cnt+1))

        if maze[y + 1][x]!=1:
            if maze[y + 1][x] == 3:
                break
            enQ(Node((x,y + 1), front.cnt+1))

        if maze[y - 1][x]!=1:
            if maze[y - 1][x] == 3:
                break
            enQ(Node((x,y - 1), front.cnt + 1))

        tmp = deQ()
    if front is not None:
        cnt=deQ()
    else:
        cnt=0
    print('#{} {}'.format(t, cnt))
