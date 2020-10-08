from collections import deque


def bfs(i, n, nl):
    # 아무 점에서나 최대거리인 점 구하기
    Q = deque([i])
    vl = [0] * (n + 1)
    vl[i] = 1
    while Q:
        c = Q.popleft()
        for j in nl[c]:
            if not vl[j]:
                vl[j] = 1
                Q.append(j)
    return bfs2(c, n, nl)


def bfs2(i, n, nl):
    # 가장 멀리 있는 점 1개 고르기
    Q = deque([[i, 0]])
    vl = [0] * (n + 1)
    vl[i] = 1
    rl = [0, 0]
    while Q:
        c, d = Q.popleft()
        rl[1] = rl[0]
        rl[0] = d
        for j in nl[c]:
            if not vl[j]:
                vl[j] = 1
                Q.append([j, d + 1])
    # 가장 멀리 있는 점이 c이다.
    rl.append(bfs3(c, n, nl, i))
    rl.sort()
    return rl[1]

def bfs3(i, n, nl, x):
    # x를 제외한 가장 멀리 있는 점 1개 고르기
    Q = deque([[i, 0]])
    vl = [0] * (n + 1)
    vl[i] = 1
    vl[x] = 1
    while Q:
        c, d = Q.popleft()
        for j in nl[c]:
            if not vl[j]:
                vl[j] = 1
                Q.append([j, d + 1])
    return d


def solution(n, edges):
    nl = [[] for _ in range(n + 1)]
    for a, b in edges:
        nl[a].append(b)
        nl[b].append(a)

    answer = bfs(1, n, nl)
    return answer

print(solution(	5, [[1, 2], [1, 3], [1, 4], [2, 5]]))