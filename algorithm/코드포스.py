l, r = map(int, input().split())
chk = 0
for i in range(l, r+1):
    tmp = str(i)
    tmp1 = set(list(tmp))
    if len(tmp) == len(tmp1):
        print(tmp)
        chk += 1
        break
if not chk:
    print(-1)