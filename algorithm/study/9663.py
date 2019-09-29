'''
시간초과
'''
def nq(dep=0):
    global R
    if dep == N:
        R += 1
        return
    for i in range(N):
        chk = 0
        for dx, dy in dr:
            for k in range(1, dep+1):
                tx = i + dx*k
                if 0 <= tx < N:
                    ty = dep + dy*k
                    if ml[ty][tx]:
                        chk = 1
                        break
                else:
                    break

            if chk:
                break
        if chk:
            continue

        ml[dep][i] = 1
        nq(dep+1)
        ml[dep][i] = 0

dr = [[-1, -1], [0, -1], [1, -1]]
N = int(input())
vl = [0 for i in range(N)]
ml = [[0 for i in range(N)] for i in range(N)]
R = 0
nq()
print(R)