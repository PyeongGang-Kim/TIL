import sys
input = sys.stdin.readline
pl = [1] * 4000001
pl[1] = 0
pl[0] = 0
i = 2
while i < 2001:
    if pl[i]:
        tmp = i ** 2
        while tmp < 4000001:
            pl[tmp] = 0
            tmp += i
    i += 1
i = 3
pl = [i for i in range(4000001) if pl[i]]

i, j = 0, 0
b = int(input())
cnt = 0
sn = pl[0]
maxlen = len(pl)
while j < maxlen:
    if sn < b:
        j += 1
        if j >= maxlen:
            break
        sn += pl[j]

    elif sn > b:
        if i == j:
            break
        sn -= pl[i]
        i += 1
    else:
        cnt += 1
        j += 1
        if j >= maxlen:
            break
        sn += pl[j]
        sn -= pl[i]
        i += 1

print(cnt)