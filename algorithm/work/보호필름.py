'''
bfs, 리스트 pop(0)제한시간 초과
bfs, 큐 런타임에러
bfs, 리스트 + front 런타임 에러
dfs, 스택 통과
'''
import sys
sys.stdin = open('asdf.txt')


def ck(arr):
    if K == 1:
        return True

    for w in range(W):
        cnt = 1
        for d in range(1, D):
            if arr[d][w] == arr[d-1][w]:
                cnt += 1
            else:
                cnt = 1
            if cnt == K:
                break
        if cnt != K:
            return False
    return True


def dfs():
    global result
    if ck(nl):
        result = 0
        return
    st = []
    for i in range(D):
        st.append([[[i, 0]], 1])
        st.append([[[i, 1]], 1])
    while st:
        tmpc, dep = st.pop()
        if mkarr(tmpc):
            if result > dep:
                result = dep
        if result < dep:
            continue

        if dep != K - 1:
            for k in range(tmpc[-1][0]+1, D):
                tmpc.append([k, 0])
                st.append([tmpc[:], dep + 1])
                tmpc.pop()
                tmpc.append([k, 1])
                st.append([tmpc[:], dep + 1])
                tmpc.pop()


def mkarr(tmpc):
    tl = nl[:]
    r = 0
    for i in tmpc:
        tl[i[0]] = E[i[1]]
    if ck(tl):
        r = 1
    if r:
        return True

    return False


T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    nl = [list(map(int, input().split())) for _ in range(D)]
    E = [[0 for _ in range(W)], [1 for _ in range(W)]]
    result = K
    tl = nl[:]
    dfs()
    print('#{} {}'.format(t, result))
