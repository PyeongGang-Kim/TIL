class Node:
    def __init__(self, ci=0, n=None):
        self.next = n
        self.ci = ci
        self.idx=0


def enQ():
    global front, rear
    newNode = Node()
    if not front:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode


def nextPizza():
    global front, result, chk
    front.ci = front.ci//2
    if front.ci!=0:
        result=front.idx
        chk=0
    front=front.next
    return


def inPizza(ci):
    global idx
    front.ci=ci
    front.idx = idx
    idx+=1


def chkQ(N):
    tmp=1
    chkQu=front
    for n in range(N):
        if chkQu.ci!=0:
            tmp=0
    return tmp




T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().strip().split(' '))
    pl = list(map(int, input().strip().split(' ')))
    idx=1
    chk=0

    front, rear = None, None
    for n in range(N):
        enQ()
    rear.next=front
    while chk<=N:
        if front.ci==0:
            if pl:
                inPizza(pl.pop(0))
                chk=0
            else:
                nextPizza()
                chk+=1
        else:
            nextPizza()


    print('#{} {}'.format(t, result))
