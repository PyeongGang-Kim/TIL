def unionfind(n):
    if cl[n]:
        tmp = unionfind(cl[n])
        cl[n] = tmp
        return tmp
    else:
        return n


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    nl = []
    for _ in range(E):
        nl.append(list(map(int, input().split())))
    nl.sort(key=lambda x: x[2])
    cl = [0 for _ in range(V+1)]

    r = 0
    for l in nl:
        a, b = unionfind(l[0]), unionfind(l[1])
        if a != b:
            cl[b] = a
            r += l[2]
    print('#{} {}'.format(t, r))