import sys
from collections import deque
'''
0, 1 냅색 문제랑 비슷하다.
asdf zxcv의 lcs를 구하려면 테이블을 이렇게 두고
    0   a   s   d   f
0   0   0   0   0   0
z
x
c
v
한 행씩 채워나간다.
현재 행의 알파벳이 현재 열의 알파벳과 같을 경우 왼쪽 대각선 위 + 1을 해주고
다른 값일 경우에는 왼쪽 혹은 위쪽 값 중 최대값을 선택한다.

모두 끝났을 경우 맨 마지막 위치에서 왼쪽 혹은 위쪽에 나랑 같은 값이 나오지 않을 때 까지 이동한 후
왼쪽 혹은 위쪽에 나랑 같은 값이 안 나오는 순간에 그 위치의 값에 -1 을 해 주고 왼쪽 대각선 위로 이동한다.
현재 값이 0 이 될 때까지 이동하면 된다.
대각선 위로 올라갈 때의 알파벳이 원하는 알파벳이 된다.
'''
A = input()
B = input()
D = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
for j in range(1, len(B)+1):
    for i in range(1, len(A)+1):
        if A[i-1] == B[j-1]:
            D[j][i] = D[j-1][i-1] + 1
        else:
            D[j][i] = max(D[j-1][i], D[j][i-1])

c = D[-1][-1]
Q = deque([])
tx, ty = len(A), len(B)
while c:
    if D[ty-1][tx] == c:
        ty -= 1
    elif D[ty][tx-1] == c:
        tx -= 1
    else:
        c -= 1
        tx -= 1
        ty -= 1
        Q.appendleft(A[tx])
print(len(Q))
print(''.join(Q))