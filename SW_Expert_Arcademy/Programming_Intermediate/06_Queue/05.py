class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n


def enQ(item):
    global front, rear
    newNode = Node(item)
    if not front:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode


def denQ():
    global front, rear
    enQ(front.item)
    front = front.next


def printQ():
    f=front
    s = ""
    while f:
        s += f.item
        f= f.next
    return s

T=int(input())
for t in range(1,T+1):

    front, rear = None, None

    N, M = map(int, input().strip().split(' '))
    nl=list(map(int, input().strip().split(' ')))
    for n in nl:
        enQ(n)
    for m in range(M):
        denQ()
    print('#{} {}'.format(t, front.item))
