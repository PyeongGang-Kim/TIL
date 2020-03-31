import sys
'''
사다리를 3개까지 설치해보고 답이 안나올 경우 -1을
답이 나올 경우 최소의 수를 출력하면 된다.
=> 사다리를 설치하지 않아도 될 경우
사다리를 한개 설치해야 할 경우
사다리를 두개 설치해야 할 경우
사다리를 세개 설치해야 할 경우
그 외의 경우
이런 조건으로 따져봐야 한다.

ladder 함수는 모든 세로선의 결과가 세로선의 인덱스와 같게 나오면 True
아닐 경우 False를 반환하는 함수이다.

pl은 사다리를 추가적으로 설치 가능한 좌표들을 모아놓은 것이다.
nl[j][i] 가 0 이고 nl[j][i-1]이 0이면 연속된 사다리가 아니므로 설치할 수 있는 곳이다.

solve(n, dep, idx)는 현재 사다리를 설치한 갯수 dep
설치하고자 하는 사다리의 갯수 n
이번에 설치할 사다리 좌표(pl에서의 인덱스)를 나타낸다.



'''
def ladder():
    chk = False
    for i in range(1, N+1):
        j = 1
        tmp = i
        while j <= H:
            if nl[j][i]:
                i += 1
            elif nl[j][i-1]:
                i -= 1
            j += 1
        if tmp != i:
            chk = True
            break
    if chk:
        return False
    return True


def solve(n, dep=0, idx=0):
    if dep == n:
        if ladder():
            return True
        return False

    for i in range(idx, len(pl)):
        if not nl[pl[i][1]][pl[i][0]-1]:
            nl[pl[i][1]][pl[i][0]] = True
            if solve(n, dep+1, i + 1):
                return True
            nl[pl[i][1]][pl[i][0]] = False


N, M, H = map(int, sys.stdin.readline().split())
nl = [[False for _ in range(N+1)] for _ in range(H+1)]
for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    nl[a][b] = True

r = 4
if ladder():
    r = 0
else:
    pl = []
    for j in range(1, H + 1):
        for i in range(1, N):
            if not nl[j][i] and not nl[j][i - 1] and not nl[j][i + 1]:
                pl.append((i, j))
    for i in range(1, 4):
        if solve(i):
            r = i
            break
if r > 3:
    print(-1)
else:
    print(r)