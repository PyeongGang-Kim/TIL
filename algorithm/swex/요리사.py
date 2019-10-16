def comb(idx=0, arr=[]):
    global r
    if len(arr) == N2:
        arr2 = []
        for k in range(N):
            if k not in arr:
                arr2.append(k)

        s1 = 0
        for j in arr:
            for i in arr:
                if i > j:
                    s1 += nl[j][i]
        s2 = 0
        for j in arr2:
            for i in arr2:
                if i > j:
                    s2 += nl[j][i]

        r = min(r, abs(s1-s2))
        return

    for i in range(idx, N-(N2-len(arr))+1):
        arr.append(i)
        comb(i+1, arr)
        arr.pop()

T = int(input())
for t in range(1, T+1):
    N = int(input())
    N2 = N//2

    nl = [list(map(int, input().split())) for _ in range(N)]
    for j in range(N-1):
        for i in range(j+1, N):
            nl[j][i] += nl[i][j]
    r = 0xffffffff
    suma = 0
    for i in range(1, N):
        suma += nl[0][i]

    comb()
    print('#%d %d' %(t, r))
