import sys
sys.stdin = open('asdf.txt')


def cntn(i):
    global cnt
    cnt += 1
    if tree[i][0]:
        cntn(tree[i][0])
    if tree[i][1]:
        cntn(tree[i][1])

T = int(input())
for t in range(1, T+1):
    V, E, P1, P2 = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    for i in range(0, len(data)-1, 2):
        if tree[data[i]][0] != 0:
            tree[data[i]][1] = data[i+1]
        else:
            tree[data[i]][0] = data[i+1]
        tree[data[i+1]][2] = data[i]



    while 1:
        if i1 + 1 == i2:
            if i1//2 == i2//2:
                break
            else:
                i1 //= 2
                i2 //= 2
                continue
        i2 //= 2
        if i1 > i2:
            i1, i2 = i2, i1
    r1 = i1//2
    cnt = 0
    print('#{} {} {}'.format(t, tree[r1], cnt))