import sys
sys.stdin = open("#4831_input.txt")

def find_st(p, cnt):
    temp = []
    if p+R >= N:
        return p, cnt
    else:
        cnt += 1
        chk = 0
        for X in range(p+1, p+R+1):
            if list_n[X]:
                temp.append(X)
                chk += 1
        if chk == 0:
            return N, 0
        return find_st(temp[-1], cnt)


for i in range(int(input())):
    R, N, C = map(int, input().strip().split(' '))
    cnt = 0
    M = list(map(int, input().strip().split(' ')))
    list_n = [int(i in M) for i in range(N + 1)]
    P=find_st(0, 0)[1]
    print('#{}'.format(i + 1), P)