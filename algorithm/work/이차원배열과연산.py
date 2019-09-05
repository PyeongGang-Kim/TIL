import sys
# sys.stdin = open('asdf.txt')


def oper():
    global nl
    if len(nl[0]) <= len(nl):
        chk = 0
    else:
        chk = 1
    tl = []
    tmplen = 0
    if chk:
        for i in range(len(nl[0])):
            tmp = {}
            for j in range(len(nl)):
                if tmp.get(nl[j][i]):
                    tmp[nl[j][i]] += 1
                else:
                    tmp[nl[j][i]] = 1
            if tmp.get(0):
                del tmp[0]
            tmp2 = []
            for k, v in tmp.items():
                tmp2.append([k, v])
            for k in range(len(tmp2)-1):
                for i in range(k, len(tmp2)):
                    if tmp2[i][1] < tmp2[i-1][1]:
                        tmp2[i], tmp2[i-1] = tmp2[i-1], tmp2[i]
            tmp2 = tmp2[:100]
            if len(tmp2)*2 > tmplen:
                tmplen = len(tmp2)*2
            tmp4 = []
            for i in tmp2:
                tmp4.append(i[0])
                tmp4.append(i[1])
            tl.append(tmp4)
        for j in range(len(tl)):
            tl[j] = tl[j] + [0] * (tmplen - len(tl[j]))
        nl = [[tl[i][j] for i in range(len(tl))] for j in range(tmplen)]
    else:
        for j in range(len(nl)):
            tmp = {}
            for i in range(len(nl[0])):
                if tmp.get(nl[j][i]):
                    tmp[nl[j][i]] += 1
                else:
                    tmp[nl[j][i]] = 1

            if tmp.get(0):
                del tmp[0]
            tmp2 = []
            for k, v in tmp.items():
                tmp2.append([k, v])
            for k in range(len(tmp2)-1):
                for i in range(k, len(tmp2)):
                    if tmp2[i][1] < tmp2[i-1][1]:
                        tmp2[i], tmp2[i-1] = tmp2[i-1], tmp2[i]
            tmp2 = tmp2[:100]
            if len(tmp2)*2 > tmplen:
                tmplen = len(tmp2)*2
            tmp4 = []
            for i in tmp2:
                tmp4.append(i[0])
                tmp4.append(i[1])
            tl.append(tmp4)
        for j in range(len(tl)):
            tl[j] = tl[j] + [0] * (tmplen - len(tl[j]))
        nl = [[tl[j][i] for i in range(tmplen)] for j in range(len(tl))]


r, c, k = map(int, input().split())
nl = [list(map(int, input().split())) for _ in range(3)]

i = 0
while i<=100:
    if 0 <= c-1 < len(nl) and 0 <= r-1 < len(nl[0]):
        if nl[c-1][r-1] == k:
            break
    oper()
    for j in range(len(nl)):
        print(nl[j])
    print(i)

    i += 1
if i > 100:
    i = -1
print(i)
