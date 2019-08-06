class Node:

    def __init__(self, num, next = None):
        global cnt
        self.num = num
        self.next = next
        cnt += 1

def enQ(num):
    global front, rear, cnt
    if front is None:
        front = Node(num)
        rear = front
    else:
        rear.next = Node(num)
        rear = rear.next

def insertQ(idx, num):
    global front, rear, cnt
    if cnt < idx:
        rear.next = Node(num)
        rear = rear.next
    else:
        tmp = front
        if idx == 0:
            front = Node(num, tmp)
        else:
            for i in range(idx-1):
                tmp = tmp.next
            tmp.next = Node(num, tmp.next)


T = int(input())
for t in range(1, T+1):
    front = None
    rear = None
    cnt = 0
    N, M, L = map(int, input().split())
    nl= map(int, input().split())
    for n in nl:
        enQ(n)
    for m in range(M):
        insertQ(*map(int, input().split()))

    tmp = front
    for l in range(L):
        tmp = tmp.next

    print('#{} {}'.format(t, tmp.num))