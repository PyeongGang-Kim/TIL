class node:
    def __init__(self, P, idx=1, n=None):
        self.P=P
        self.next=n
        self.idx=idx


def enQ(P, idx=-1):
    global front, rear, Visit
    idx+=1

    Visit[P-1]=1
    if front == None:
        front=node(P, idx)
        rear=front
    else:
        rear.next=node(P, idx)
        rear=rear.next


def fndQ(P):
    global front, rear, listE, G, Visit
    for e in listE:
        if P in e:
            tmp=e-{P}
            tmp2=tmp.pop()
            if not Visit[tmp2-1]:
                if tmp2 == G:
                    return 1
                enQ(tmp2, front.idx)
    return 0


def deQ():
    global front, rear, chk, idx, result
    chk = fndQ(front.P)
    if chk:
        result= front.idx+1
        return
    if front==rear:
        chk=1
        result=0
    else:
        result=front.idx+1
        front=front.next


T=int(input())
for t in range(1,T+1):
    #V 노드 갯수 E간선 갯수
    V, E = map(int, input().split())
    #간선 셋이 담긴 리스트 listE
    listE=[set(map(int, input().split())) for i in range(E)]
    #S 시작점, G 도착점
    S, G = map(int, input().split())
    #방문 리스트 Visit
    Visit=[0]*V
    front, rear = None, None
    idx=0
    enQ(S)
    chk=0
    while not chk:
        deQ()
    print('#{} {}'.format(t,result))
