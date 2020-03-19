def comb(idx = 0, arr = []):
    if len(arr) == L:
        cnt1 = 0
        cnt2 = 0
        for i in range(L):
            if arr[i] in {'a', 'e', 'i', 'o', 'u'}:
                cnt1 = 1
            else:
                cnt2 += 1
        if cnt1 and cnt2 >1:
            print(''.join(arr))
        return

    for i in range(idx, C - (L - len(arr)) + 1):
        arr.append(d[i])
        comb(i+1, arr)
        arr.pop()

L, C = map(int, input().split())
d = sorted(input().split())
comb()