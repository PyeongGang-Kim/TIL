import sys

'''
싸이클에 있는 원소들의 갯수와 싸이클에 있는 원소들을 출력하면 된다.

'''

def dfs(i):
    global fnd, cnt, chk
    #현재 사이클 만남
    if vl1[nl[i]]:
        vl2[i] = True
        if nl[i] == i:
            cnt += 1
        else:
            fnd = nl[i]
            cnt += 1
            chk = True
        r.append(i+1)
        return

    # 사이클에 존재할 수가 없는 곳이 아닐 때
    elif not vl2[nl[i]]:
        vl1[nl[i]] = True
        dfs(nl[i])
        vl1[nl[i]] = False
        if chk:
            if i == fnd:
                chk = False
            cnt += 1
            r.append(i+1)

    # 더 이상 진행할 곳이 없을 때
    vl2[i] = True
    return

N = int(sys.stdin.readline())
nl = [int(sys.stdin.readline())-1 for _ in range(N)]
vl1 = [False for _ in range(N)]
vl2 = [False for _ in range(N)]
cnt = 0
fnd = 0
r = []
for i in range(N):
    if not vl2[i]:
        vl1[i] = True
        chk = False
        dfs(i)
        vl1[i] = False
print(cnt)
r.sort()
r2 = []
for n in r:
    r2.append(str(n))
print('\n'.join(r2))