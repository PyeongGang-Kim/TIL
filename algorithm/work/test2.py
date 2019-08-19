T = 10
for t in range(1, T+1):
    nnnnn = input()
    nl = list(map(int, input().split()))
    nnnn = int(input())
    ol = input().split()
    for k in range(nnnn):
        ol.pop(0)
        i = int(ol.pop(0))
        n = int(ol.pop(0))
        if i < 10:
            for k in range(n):
                nl.insert(i, ol.pop(0))
        else:
            for k in range(n):
                ol.pop(0)
    print('#{}'.format(t), end='')
    for i in range(10):
        print(' {}'.format(nl.pop(0)), end='')

