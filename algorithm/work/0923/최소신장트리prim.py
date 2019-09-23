import sys
sys.stdin = open('최소신장트리.txt')

def prim(idx = 0):
    global ad, r

    while ad:
        id = -1
        tmpd = 11
        idl = []
        for i in range(len(ad)):
            if ad[i][1] <= tmpd:
                if ad[i][0] not in tmp:
                    id = i
                    tmpd = ad[i][1]
                else:
                    idl.append(i)
        if id != -1:
            tmp.add(ad[id][0])
            r += ad[id][1]
            ad += nl[ad[id][0]][:]
        while idl:
            i2 = idl.pop()
            ad[-1], ad[i2] = ad[i2], ad[-1]
            ad.pop()


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    nl = {i: [] for i in range(V+1)}
    for e in range(E):
        n1, n2, d = map(int, input().split())
        nl[n1].append([n2, d])
        nl[n2].append([n1, d])
    tmp = {0}
    r = 0
    ad = nl[0][:]
    prim()
    print('#{} {}'.format(t, r))