T=int(input())
for t in range(1, T+1):
    b=int(input())
    c=list(map(int, input().split(" ")))
    min, max = c[0], c[0]
    for s in c:
        if min > s:
            min = s
        if max < s:
            max = s

    print('#{} {}'.format(t, max-min))