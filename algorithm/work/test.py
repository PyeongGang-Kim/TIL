import sys
sys.stdin = open('asdf.txt')

'''


'''
def chk():
    for j in range(R):
        for i in range(C):
            if nl[j][i] == '@':
                return True
    return False


def dfs(x=0, y=0, d=2, m=0):
    st.append([x, y, d, m])
    while st:
        x, y, d, m = st.pop()
        if nl[y][x] == '<':
            d = 3
            chk2(x, y, d, m)
        elif nl[y][x] == '>':
            d = 2
            chk2(x, y, d, m)
        elif nl[y][x] == '^':
            d = 1
            chk2(x, y, d, m)
        elif nl[y][x] == 'v':
            d = 0
            chk2(x, y, d, m)
        elif nl[y][x] == '_':
            if m:
                d = 3
                chk2(x, y, d, m)
            else:
                d = 2
                chk2(x, y, d, m)
        elif nl[y][x] == '|':
            if m:
                d = 1
                chk2(x, y, d, m)
            else:
                d = 0
                chk2(x, y, d, m)
        elif nl[y][x] == '?':
            for i in range(4):
                chk2(x, y, i, m)
        elif nl[y][x] == '.':
            chk2(x, y, d, m)
        elif nl[y][x] == '@':
            return True
        elif nl[y][x] == '+':
            m = (m + 1) % 16
            chk2(x, y, d, m)
        elif nl[y][x] == '-':
            m = (m - 1) % 16
            chk2(x, y, d, m)
        else:
            m = int(nl[y][x])
            chk2(x, y, d, m)


def chk2(x, y, d, m):
    x = (x + dr[d][0]) % C
    y = (y + dr[d][1]) % R
    tmp1 = str(x) + str(y) + str(d) + str(m)
    if tmp1 not in tmp:
        tmp.add(tmp1)
        st.append([x, y, d, m])


dr = [[0, 1], [0, -1], [1, 0], [-1, 0]]
T = int(input())
for t in range(1, T + 1):
    tmp = set()
    st = []
    tmp = set()
    R, C = map(int, input().split())
    nl = [input() for _ in range(R)]
    if chk() and dfs():
        print('#%d YES' %t)
    else:
        print('#%d NO' %t)