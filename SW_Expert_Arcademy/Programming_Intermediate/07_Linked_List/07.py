class Node:
    def __init__(self, num, b=None, n=None):
        self.num = num
        self.b = b
        self.n = n


def enQ(num):
    global front, rear
    if front is None:
        front = Node(num)
        rear = front
    else:
        tmp = rear
        rear = Node(num)
        rear.b = tmp
        tmp.n = rear


def cirQ():
    global front, rear
    rear.n = front
    front.b = rear


def insQ(p, idx):
    global front, position, posn
    if posn:
        tmp = posn
    else:
        tmp = front
    cnt = 0
    for i in range(p):
        tmp = tmp.n
    for i in range(idx-1):
        tmp = tmp.n
    tmp2 = tmp.n
    new_node = Node(tmp.num+tmp2.num, tmp, tmp2)
    tmp.n = new_node
    tmp2.b = new_node
    posn = tmp.n


T = int(input())

for t in range(1,T+1):
    front, rear, posn = None, None, None
    N, M, K = map(int, input().split())
    nl = list(map(int, input().split()))

    for n in nl:
        enQ(n)

    cirQ()
    position = 0
    for k in range(K):
        insQ(position, M)
    tmp = front
    result = ''
    for i in range(10):
        tmp = tmp.b
        if front == tmp:
            result += ' ' + str(tmp.num)
            break
        result += ' ' + str(tmp.num)

    print('#{}{}'.format(t, result))