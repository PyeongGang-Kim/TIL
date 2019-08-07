class Node:
    def __init__(self, num, child1 = None, child2 = None):
        self.num = num
        self.child1 = child1
        self.child2 = child2


def cntC(num):
    global Tree
    idx = num - 1
    if Tree[idx].child1 is None:
        return 1
    else:
        cnt = cntC(Tree[idx].child1.num)
        if Tree[idx].child2:
            cnt += cntC(Tree[idx].child2.num)
        return cnt + 1

T = int(input())
for t in range(1, T+1):

    E, N = map(int, input().split())
    Tree = []
    for n in range(1, E+2):
        Tree.append(Node(n))
    nl = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        if Tree[nl[i]-1].child1 is None:
            Tree[nl[i]-1].child1 = Tree[nl[i+1]-1]
        else:
            Tree[nl[i]-1].child2 = Tree[nl[i+1]-1]

    result = cntC(N)
    print('#{} {}'.format(t, result))