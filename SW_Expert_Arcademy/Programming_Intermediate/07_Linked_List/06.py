class Node:
    def __init__(self, num, before = None, next = None):
        self.num = num
        self.next = next
        self.before = before


def enQ(f, r, num):
    if f is None:
        f = Node(num)
        r = f
    else:
        tmp = r
        tmp.next = Node(num, r)
        r=tmp.next

    return f, r


def insQ():
    global front, rear, front2, rear2
    tmp = front
    if tmp.num > front2.num:
        front = front2
        rear2.next = tmp
        tmp.before = rear2
    else:
        while tmp.num:
            if tmp.num > front2.num:
                rear2.next = tmp
                front2.before = tmp.before
                tmp.before.next = front2
                tmp.before=rear2
                break
            if tmp.next is not None:
                tmp = tmp.next
            else:
                front2.before = rear
                rear.next = front2
                rear = rear2
                break

    if tmp is None:
        rear.next = front2
        front2.before = rear
        rear = rear2

def printQ():
    global rear
    result = ''
    tmp = rear
    for i in range(10):
        result += ' ' +str(tmp.num)
        tmp=tmp.before
    return result


T=int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    front, rear = None, None

    ml = map(int, input().split())
    for num in ml:
        front, rear = enQ(front, rear, num)

    for m in range(M-1):
        front2, rear2 = None, None
        ml2 = map(int, input().split())
        for num in ml2:
            front2, rear2 = enQ(front2, rear2, num)
        insQ()
    print('#{}{}'.format(t, printQ()))