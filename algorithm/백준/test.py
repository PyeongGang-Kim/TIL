import sys


# import heapq
# input = sys.stdin.readline
# sys.stdin = open('input.txt', encoding='utf8')

def ria():
    return list(map(int, input().split()))


sys.setrecursionlimit(100000)


def solve():
    v, e = ria()
    # print(v,e)

    visited = [False] * (v + 10)
    finished = [False] * (v + 10)
    adj = [[] for x in range(e + 10)]
    stack = []
    curScc = []
    SCC = []
    dfsn = [0] * (v + 10)
    curn = 1

    for i in range(e):
        a, b = ria()
        adj[a].append(b)

    def dfs(cur):
        nonlocal stack, curScc, SCC, dfsn, curn, adj, visited, finished

        stack.append(cur)

        dfsn[cur] = curn
        curn += 1

        result = dfsn[cur]

        for there in adj[cur]:
            if (dfsn[there] == 0):
                result = min(result, dfs(there))
            elif (not finished[there]):
                result = min(result, dfsn[there])

        if (result == dfsn[cur]):
            curScc = []
            while (True):
                tt = stack.pop()
                curScc.append(tt)
                finished[tt] = True
                if (tt == cur): break
            curScc.sort()
            SCC.append(curScc)

        return result

    for i in range(1, v + 1):
        if (dfsn[i] == 0): dfs(i)

    # print(adj)  
    # print(dfsn)
    SCC.sort()
    # print(SCC)

    print(len(SCC))
    for i, sc in enumerate(SCC):
        print(' '.join(map(str, sc)) + ' -1')
solve()