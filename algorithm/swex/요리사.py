def com(arr1=[], arr2=[], idx = 0):
    global result
    if result == 0:
        return
    if len(arr1) > N2 or len(arr2) > N2:
        return
    if idx == N:
        f1 = 0
        f2 = 0
        for i in range(N2-1):
            for j in range(i+1, N2):
                f1 += nl[arr1[i]][arr1[j]]
                f2 += nl[arr2[i]][arr2[j]]
        result = min(result, abs(f1-f2))
        return
    arr1.append(idx)
    com(arr1, arr2, idx+1)
    arr1.pop()
    arr2.append(idx)
    com(arr1, arr2, idx+1)
    arr2.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N2 = N//2
    nl = [list(map(int, input().split())) for _ in range(N)]
    for j in range(N-1):
        for i in range(j+1, N):
            nl[j][i] += nl[i][j]
    result = 0xffffffff
    com()
    print('#{} {}'.format(tc, result))