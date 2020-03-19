'''
update를 사용해서 시간을 단축할 수 있다.
매 번 반복할 때마다 갱신이 이루어졌으면 수행
갱신이 안 이루어졌으면 중지
다 돌고 나서 마지막 n번째에서도 갱신이 됐다면 true반환.
true 반환이 되면 음의 사이클이 존재한다는 의미이다
매 번마다 false로 두고 갱신이 있을 때에만 실시한다.

아니라면

최단 경로의 거리를 찾을 필요가 없이 음의 사이클만 존재하면 되므로
무한대인 정점이라도 갱신을 시작해도 상관이 없다.

'''

import sys
input = sys.stdin.readline

def check():
    nl = [inf] * (N + 1)
    nl[1] = 0
    n = N
    update = False
    while n:
        update = False
        for s, e, t in ml:
            if nl[s] + t < nl[e]:
                update = True
                nl[e] = nl[s] + t
        n -= 1
        if not update:
            break
    if update:
        return True
    return False


inf = 0xfffffff
TC = int(input())

while TC:
    TC -= 1

    N, M, W = map(int, input().split())
    ml = []
    while M:
        M -= 1
        S, E, T = map(int, input().split())
        ml.append([S, E, T])
        ml.append([E, S, T])
    while W:
        W -= 1
        S, E, T = map(int, input().split())
        ml.append([S, E, -T])


    if check():
        print('YES')
    else:
        print('NO')