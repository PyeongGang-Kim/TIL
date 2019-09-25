def unionfind(n):
    if cl[n]:
        tmp = unionfind(cl[n])
        cl[n] = tmp
        return tmp
    return n


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    cl = [0 for _ in range(n+1)]
    r = ['#%d ' %t]
    for _ in range(m):
        o, a, b = map(int, input().split())
        t1, t2 = unionfind(a), unionfind(b)
        if o:
            if t1 == t2:
                r.append('1')
            else:
                r.append('0')
        else:
            if t1 != t2:
                cl[t2] = t1
    print(''.join(r))