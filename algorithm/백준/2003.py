a, b = map(int, input().split())
nl = list(map(int, input().split()))
i, j = 0, 0

cnt = 0
sn = nl[0]
while j < a:
    if sn < b:
        j += 1
        if j >= a:
            break
        sn += nl[j]
    elif sn > b:
        if i == j:
            j += 1
            if j >= a:
                break
            sn += nl[j]
        sn -= nl[i]
        i += 1
    else:
        cnt += 1
        j += 1
        if j >= a:
            break
        sn += nl[j]
        sn -= nl[i]
        i += 1

print(cnt)