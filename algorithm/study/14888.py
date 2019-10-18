def comb(arr=[]):
    global r, r2
    if len(arr) == N-1:
        tmp = nl[0]
        for i in range(len(arr)):
            if arr[i] == 0:
                tmp += nl[i+1]
            elif arr[i] == 1:
                tmp -= nl[i+1]
            elif arr[i] == 2:
                tmp *= nl[i+1]
            elif arr[i] == 3:
                if tmp < 0:
                    tmp = -((-tmp)//nl[i+1])
                else:
                    tmp //= nl[i+1]
        r = min(r, tmp)
        r2 = max(r2, tmp)
        return
    for i in range(4):
        if O[i] > vl[i]:
            arr.append(i)
            vl[i] += 1
            comb(arr)
            arr.pop()
            vl[i] -= 1


N = int(input())
nl = list(map(int, input().split()))
O = list(map(int, input().split()))
vl = [0]*4
r = 1000000000
r2 = -r
comb()
print(r2)
print(r)
