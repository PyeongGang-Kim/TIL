import sys
sys.stdin = open('asdf.txt')

def C(d=0, s=''):
    tmp = 0
    if d == 6:
        if chkrungin(s[0:3]) and chkrungin(s[3:]):
            return 1
        return 0
    for i in range(6):
        if not vl[i]:
            vl[i] = 1
            tmp = C(d+1, s+nu[i])
            vl[i] = 0
            if tmp:
                break
    return tmp


def chkrungin(S):
    if S[0] == S[1] and S[1] == S[2]:
        return 1
    if int(S[0]) == int(S[1])+1 and int(S[1]) == int(S[2])+1:
        return 1


T = int(input())
for t in range(1, T+1):
    vl = [0]*6
    nu = input()
    chk = 0
    print(C())