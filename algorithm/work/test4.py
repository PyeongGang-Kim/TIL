import sys
sys.stdin = open('asdf.txt')


def dfs(s):
    global r
    if chk():
        r = s
    if r != 'impossible':
        return
    if s[-1] == '0':
        if vl[0]:
            vl[0]-=1
            dfs(s+'0')
            vl[0]+=1
        if vl[1]:
            vl[1]-=1
            dfs(s+'1')
            vl[1]+=1
    else:
        if vl[2]:
            vl[2]-=1
            dfs(s+'0')
            vl[2]+=1
        if vl[3]:
            vl[3]-=1
            dfs(s+'1')
            vl[3]+=1


def chk():
    for i in range(4):
        if vl[i] != 0:
            return False
    return True


rr = ['00', '01', '10', '11']
T = int(input())
for t in range(1, T+1):
    vl = list(map(int, input().split()))
    r = 'impossible'
    t1 = max(vl[1], vl[2])
    t2 = min(vl[0], vl[3])
    if t1<t2:
        pass
    else:
        for i in range(4):
            if r != 'impossible':
                break
            if vl[i]:
                vl[i]-=1
                dfs(rr[i])
                vl[i]+=1
    print('#{} {}'.format(t, r))
