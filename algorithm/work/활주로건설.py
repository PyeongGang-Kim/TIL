'''
내 위치부터 경사로길이까지 한칸씩 탐색한다.
만약 경사로길이까지 안갔는데 나보다 높은곳이면 활주로 불가능
경사로길이까지 안갔는데 나보다 두칸 이상 낮은곳이면 활주로 불가능
나보다 한칸 낮은곳이면 해당 위치에서 내려가는경사로 설치할 수 있는지 확인하기
내려가는경사로 만들수 없으면 활주로 불가능
내려가는경사로 만들수 있으면 그 위치로 이동한다.
만약 위치가 범위를 벗어나버리면 활주로 불가능하다.
내가 마지막 위치에 오게 되면 활주로 가능
반복.

'''
import sys
sys.stdin = open('asdf.txt')


def chk1(j):
    P = 0
    while P < N-1:
        if P + X <= N - 1 and ml[j][P] == ml[j][P+X] - 1:
            if chk2(P, j):
                P += X
                continue
            else:
                return False

        if ml[j][P] == ml[j][P+1]:
            P += 1
            continue
        elif ml[j][P] == ml[j][P+1] + 1:
            if chk2(P+1, j):
                P += X + 1
                if P > N-1:
                    return True
                if ml[j][P] != ml[j][P-1]:
                    P -= 1
                continue
            else:
                return False
        else:
            return False
    return True


def chk2(i, j):
    if i + X > N:
        return False
    tmp = ml[j][i]
    for x in range(X):
        if ml[j][i+x] != tmp:
            return False
    return True


def chk3(i):
    P = 0
    while P < N-1:
        if P + X <= N - 1 and ml[P][i] == ml[P+X][i] - 1:
            if chk4(i, P):
                P += X
                continue
            else:
                return False

        if ml[P][i] == ml[P+1][i]:
            P += 1
            continue
        elif ml[P][i] == ml[P+1][i] + 1:
            if chk4(i, P+1):
                P += X + 1
                if P > N-1:
                    return True
                if ml[P][i] != ml[P-1][i]:
                    P -= 1
                continue
            else:
                return False
        else:
            return False
    return True


def chk4(i, j):
    if j + X > N:
        return False
    tmp = ml[j][i]
    for x in range(X):
        if ml[j+x][i] != tmp:
            return False
    return True


T = int(input())
for t in range(1, T+1):
    N, X = map(int, input().split())
    ml = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if chk1(i):
            cnt += 1
        if chk3(i):
            cnt += 1
    print('#{} {}'.format(t, cnt))

