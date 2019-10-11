from collections import deque
'''
각 명령어들에 대해서 bfs(값, 명령어리스트)

시간초과
'''
def solve():
    tmpset = {A}
    Q = deque([(A, '')])
    while Q:
        nu, ops = Q.popleft()

        if nu == B:
            print(ops)
            return
        nnu = int(nu)
        tmp = str(nnu*2%10000)
        if len(tmp) != 4:
            tmp = '0'*(4-len(tmp)) + tmp
        if tmp not in tmpset:
            Q.append((tmp, ops+'D'))
            tmpset.add(tmp)
        if nnu:
            tmp = str(nnu-1)
            if len(tmp) != 4:
                tmp = '0' * (4 - len(tmp)) + tmp
            if tmp not in tmpset:
                Q.append((tmp, ops + 'S'))
                tmpset.add(tmp)
        else:
            if tmp not in tmpset:
                Q.append(('9999', ops + 'S'))
                tmpset.add('9999')
        tmp = nu[1:]+nu[0]
        if tmp not in tmpset:
            Q.append((tmp, ops+'L'))
            tmpset.add(tmp)
        tmp = nu[3]+nu[:3]
        if tmp not in tmpset:
            Q.append((tmp, ops+'R'))
            tmpset.add(tmp)

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    while len(A) != 4:
        A = '0' + A
    while len(B) != 4:
        B = '0' + B
    solve()