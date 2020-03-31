import sys
input = sys.stdin.readline


N, S = map(int, input().split())
nl = list(map(int, input().split()))

i, j = 0, 0
sn = nl[0]
maxlen = len(nl)
cnt = maxlen + 1
while j < maxlen:
    if sn < S:
        j += 1
        if j >= maxlen:
            break
        sn += nl[j]

    elif sn > S:
        cnt = min(cnt, j - i)
        if i == j:
            break
        sn -= nl[i]
        i += 1
    else:
        cnt = min(cnt, j - i)
        j += 1
        if j >= maxlen:
            break
        sn += nl[j]
        sn -= nl[i]
        i += 1
if cnt == maxlen + 1:
    print('0')
else:
    print(cnt + 1)