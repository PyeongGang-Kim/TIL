from collections import deque
# N 원판의 수, M 원판에 숫자의 수, T 명령의 수
N, M, T = map(int, input().split())
nl = [deque(list(map(int, input().split()))) for _ in range(N)]
cnt = N * M
# x배수 원판들 d 방향(0일때 시계 1일때 반시계) k 번 이동
ol = [list(map(int, input().split())) for _ in range(T)]
tim = 0
D = [[0, 1], [0, -1], [-1, 0], [1, 0]]
r = -1
while tim < T:

    # 회전 명령
    for i in range(ol[tim][0]-1, N, ol[tim][0]):
        # 반시계
        if ol[tim][1]:
            for nnn in range(ol[tim][2]):
                nl[i].append(nl[i].popleft())
        # 시계
        else:
            for nnn in range(ol[tim][2]):
                nl[i].appendleft(nl[i].pop())

    # 같은 수들을 찾기
    chk = False
    vl = [[False for _ in range(M)] for _ in range(N)]
    for j in range(N):
        for i in range(M):
            if nl[j][i] and not vl[j][i]:
                Q = [[i, j]]
                front = 0
                rear = 1
                vl[j][i] = True
                while front < rear:
                    x, y = Q[front]
                    front += 1
                    for dx, dy in D:
                        tx, ty = (x + dx) % M, y + dy
                        if 0 <= ty < N and not vl[ty][tx] and nl[ty][tx] == nl[j][i]:
                            Q.append([tx, ty])
                            vl[ty][tx] = True
                            rear += 1
                if len(Q) > 1:
                    chk = True
                    for x, y in Q:
                        nl[y][x] = 0
                        cnt -= 1

    # cnt가 0이면
    if not cnt:
        r = 0
        break
    #한번도 체크되지 않았다면
    if not chk:
        ns = 0
        for j in range(N):
            for i in range(M):
                ns += nl[j][i]
        na = ns/cnt
        for j in range(N):
            for i in range(M):
                if nl[j][i] and nl[j][i] < na:
                    nl[j][i] += 1
                elif nl[j][i] and nl[j][i] > na:
                    nl[j][i] -= 1
    tim += 1

if not r:
    print(r)
else:
    r = 0
    for j in range(N):
        for i in range(M):
            r += nl[j][i]
    print(r)