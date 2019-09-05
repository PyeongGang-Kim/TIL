import sys
sys.stdin = open('asdf.txt')

def chk():
    for j in range(9):
        tmp = set()
        for i in range(9):
            tmp.add(nl[j][i])
        if len(tmp) != 9:
            return False

    for i in range(9):
        tmp = set()
        for j in range(9):
            tmp.add(nl[j][i])
        if len(tmp) != 9:
            return False

    for j in range(3):
        for i in range(3):
            tmp = set()
            for k in range(3):
                for l in range(3):
                    tmp.add(nl[j*3+k][i*3+l])
            if len(tmp) != 9:
                return False
    return True

T = int(input())
for t in range(1, T+1):
    nl = [list(map(int, input().split())) for _ in range(9)]
    if chk():
        print('#{} {}'.format(t, 1))
    else:
        print('#{} {}'.format(t, 0))
