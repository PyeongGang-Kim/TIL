
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
        if not (-2000 <= al[i][0] <= 2000 and -2000 <= al[i][1] <= 2000):
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
    for A in al:
        A[0] = A[0]*2
        A[1] = A[1]*2

    while len(al)>1:
        ck2()
        moa()

    print('#{} {}'.format(t, E))