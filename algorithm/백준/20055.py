from collections import deque

N, K = map(int, input().split())
nl = deque([[x, 0] for x in map(int, input().split())])

def solve(N, K):
    turn = 0
    while K > 0:
        turn += 1
        chk = 0
        nl.appendleft(nl.pop())
        if nl[N-1][1]:
            nl[N-1][1] = 0
        for i in range(N-2, 0, -1):
            if nl[i][1]:
                if nl[i+1][0] and not nl[i+1][1]:
                    nl[i][1] = 0
                    nl[i+1][0] -= 1
                    if not nl[i+1][0]:
                        K -= 1
                        if not K:
                            break
                    if i != N - 2:
                        nl[i+1][1] = 1
        if chk:
            return turn
        if nl[0][0]:
            nl[0][1] = 1
            nl[0][0] -= 1
            if not nl[0][0]:
                K -= 1
                if not K:
                    return turn
    return turn

print(solve(N, K))