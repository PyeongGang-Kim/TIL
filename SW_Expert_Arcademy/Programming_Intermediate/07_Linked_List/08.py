class Node:
    def __init__(self, num, n=None):
        self.num = num
        self.n = n

def enQ(num):
    global front, rear, length
    length += 1
    if front is None:
        front = Node(num)
        rear = front
    else:
        rear.n = Node(num)
        rear = rear.n


def insQ(idx, num):
    global front, rear, length
    length += 1
    if idx == 0:
        tmp = Node(num, front)
        front = tmp
    elif idx == length-1:
        rear.n = Node(num)
        rear = rear.n
    else:
        tmp = front
        for i in range(idx-1):
            tmp = tmp.n
        tmp2 = Node(num, tmp.n)
        tmp.n = tmp2

def deQ(idx):
    global front, length
    length -= 1
    if idx == 0:
        front = front.n
    elif idx >= length:
        pass
    else:
        tmp = front
        for i in range(idx-1):
            tmp = tmp.n
        tmp.n = tmp.n.n


def chnQ(idx, num):
    global front
    tmp = front
    if idx:
        for i in range(idx):
            tmp = tmp.n
    tmp.num = num


T = int(input())
for t in range(1, T+1):
    front, rear, length = None, None, 0
    N, M, L = map(int, input().split())
    nl = map(int, input().split())
    for n in nl:
        enQ(n)
    for m in range(M):
        tmpl = list(input().split())
        if tmpl[0] == 'D':
            deQ(int(tmpl[1]))
        elif tmpl[0] == 'C':
            chnQ(int(tmpl[1]), int(tmpl[2]))
        else:
            insQ(int(tmpl[1]), int(tmpl[2]))
    if L == 0:
        result = front.num
    elif length <= L:
        print('#{} {}'.format(t, -1))
    else:
        tmp = front
        for l in range(L):
            tmp = tmp.n
        result = tmp.num
        print('#{} {}'.format(t, result))
