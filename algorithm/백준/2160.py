def comb(arr = [], i = 1):
    if len(arr) == 2:
        cnt = 0
        for j in range(5):
            for i in range(7):
                if nl[arr[0]-1][j][i] != nl[arr[1]-1][j][i]:
                    cnt += 1
        global r, R
        if r > cnt:
            r = cnt
            R = arr[:]
        return
    for idx in range(i, N+1):
        arr.append(idx)
        comb(arr, idx+1)
        arr.pop()


N = int(input())
nl = [[input() for _ in range(5)] for _ in range(N)]
r = 35
R = ''
comb()
print(R[0], R[1])