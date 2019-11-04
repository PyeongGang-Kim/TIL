def perm(arr = []):
    if len(arr) == M:
        global r
        r.add(tuple(arr))
        return
    for i in range(N):
        if not vl[i]:
            vl[i] = True
            arr.append(nl[i])
            perm(arr)
            arr.pop()
            vl[i] = False


N, M = map(int, input().strip().split())

nl = list(map(int, input().strip().split()))
vl = [False for _ in range(N)]
r = set()
perm()
r = sorted(list(r))
for rr in r:
    for rrr in rr:
        print(rrr, end=' ')
    print()
