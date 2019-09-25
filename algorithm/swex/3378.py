for t in range(1, int(input())+1):
    p, q = map(int, input().split())
    nl = []
    a, b, c = 0, 0, 0
    for i in range(p):
        s = input()
        chk = 1
        d = 0
        for j in s:
            if chk:
                if j == '.':
                    d += 1
                else:
                    chk = 0
            if j == '(':
                a += 1
            elif j == ')':
                a -= 1
            elif j == '{':
                b += 1
            elif j == '}':
                b -= 1
            elif j == '[':
                c += 1
            elif j == ']':
                c -= 1
        nl.append([a, b, c, 0])
        nl[i-1][3] = d
    nl.pop()
    print(nl)
    for i in range(len(nl)):
        if nl[i][0]:
            break
    nl[0], nl[i] = nl[i], nl[0]
    nl[0] = [nl[0][0]/nl[0][0], nl[0][1]/nl[0][0], nl[0][2]/nl[0][0], nl[0][3]/nl[0][0]]
    for i in range(1, len(nl)):
        nl[i] = [0, nl[i][1]-nl[0][1]*nl[i][0], nl[i][2]-nl[0][2]*nl[i][0], nl[i][3]-nl[0][3]*nl[i][0]]
    for i in range(1, len(nl)):
        if nl[i][1]:
            break
    nl[1], nl[i] = nl[i], nl[1]
    for i in range(2, len(nl)):
        nl[i] = [0, 0, nl[i][2]-nl[1][2]*nl[i][1], nl[i][3]-nl[1][3]*nl[i][1]]

    print(nl)

    for i in range(2, len(nl)):
        if nl[i][2]:
            break
    nl[2], nl[i] = nl[i], nl[2]
    print(nl)
    nl[2] = [0, 0, 1, nl[2][3]/nl[2][2]]


    nl[0][3] = nl[0][3] - nl[2][3] * nl[0][2]
    nl[1][3] = nl[1][3] - nl[2][3] * nl[1][2]
    nl[0][2] = nl[0][2] - nl[1][3] * nl[0][2]
    R, C, S = round(nl[0][3]), round(nl[1][3]), round(nl[2][3])

    nl = []
    a, b, c = 0, 0, 0
    for i in range(p):
        nl.append(R*a+C*b+S*c)
        if i == p-1:
            break
        P = input()
        chk = 1
        d = 0
        for j in P:
            if chk:
                if j == '.':
                    d += 1
                else:
                    chk = 0
            if j == '(':
                a += 1
            elif j == ')':
                a -= 1
            elif j == '{':
                b += 1
            elif j == '}':
                b -= 1
            elif j == '[':
                c += 1
            elif j == ']':
                c -= 1

    nl.pop()
    print(nl)