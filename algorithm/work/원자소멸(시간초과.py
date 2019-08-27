
def ck():
    global E
    for i in range(0, len(al)-1):
        for j in range(i, len(al)):
            if al[j][0] == al[i][0] + dr[al[i][2]][0] and al[j][1] == al[i][1] + dr[al[i][2]][1]:
                if al[i][2] == 1 or al[i][2] == 3:
                    if al[j][2] == al[i][2] - 1:
                        E += al[i][3] + al[j][3]
                        al.pop(j)
                        al.pop(i)
                        break
                else:
                    if al[j][2] == al[i][2] + 1:
                        E += al[i][3] + al[j][3]
                        al.pop(j)
                        al.pop(i)
                        break

def ck2():
    tmp = []
    C = []
    for A in al:
        tx, ty = A[0] + dr[A[2]][0], A[1] + dr[A[2]][1]
        if (tx, ty) not in tmp:
            tmp.append((tx, ty))
        else:
            if (tx, ty) not in C:
                C.append((tx, ty))
    while C:
        dela(*C.pop())


def dela(x, y):
    global E
    tmp = []
    for i in range(len(al)):
        if al[i][0]+dr[al[i][2]][0] == x and al[i][1]+dr[al[i][2]][1] == y:
            E += al[i][3]

            tmp.append(i)

    while tmp:
        al.pop(tmp.pop())


def moa():
    tmp = []
    for i in range(len(al)):
        al[i][0] += dr[al[i][2]][0]
        al[i][1] += dr[al[i][2]][1]
        if not (-1000 <= al[i][0] <= 1000 and -1000 <= al[i][1] <= 1000):
            tmp.append(i)
    while tmp:
        al.pop(tmp.pop())


dr = [[0, 1], [0, -1], [-1, 0], [1, 0]]
T = int(input())
for t in range(1, T+1):
    # x, y일때 M[1000-y][1000+x]
    N = int(input())
    al = []
    E = 0
    for n in range(N):
        # al = 원자 리스트 x, y, 방향(0123상하좌우), 에너지
        al.append(list(map(int, input().split())))

    while len(al)>1:
        ck()
        ck2()
        moa()

    print('#{} {}'.format(t, E))