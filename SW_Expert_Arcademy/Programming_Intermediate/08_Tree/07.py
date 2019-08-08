class NodeT:
    cnt = 0

    def __init__(self, i = None, num = None, l = None, r = None):
        NodeT.cnt += 1
        self.i = i
        self.num = num
        self.l = l
        self.r = r


class NodeQ:
    def __init__(self, item, n = None):
        self.item = item
        self.n = n


def enQ(item):
    global front, rear
    if front is None:
        front = NodeQ(item)
        rear = front
    else:
        rear.n = NodeQ(item)
        rear = rear.n


def deQ():
    global front, rear
    tmp = None
    if front:
        if rear == front:
            tmp = rear.item
            front, rear = None, None
        else:
            tmp = front.item
            front = front.n
    return tmp


def enT(num):
    global root, front, rear, N
    while NodeT.cnt < num:

        if root is None:
            root = NodeT(1)
            enQ(root)
        else:
            tmp = deQ()
            tmp.l = NodeT(NodeT.cnt + 1)


            enQ(tmp.l)
            if NodeT.cnt != num:
                tmp.r = NodeT(NodeT.cnt + 1)
                enQ(tmp.r)


def insT(nodeT):
    global nl, N, result
    NN = N//2
    if nodeT.l:
        if not nodeT.l.num:
            insT(nodeT.l)
    if nl:
        nodeT.num=nl.pop(0)
        if nodeT.i == NN:
            result = nodeT.num

    if nodeT.r:
        if not nodeT.r.num:
            insT(nodeT.r)
            return

T=int(input())
for t in range(1, T + 1):

    root, front, rear, result = None, None, None, None
    NodeT.cnt = 0
    N = int(input())
    nl = list(range(1, N + 1))
    enT(N)
    insT(root)


    print("#{} {} {}".format(t,root.num, result))