t = int(input())
for tc in range(t):
    x, y = map(int, input().split())
    tmp = x-y
    chk = False
    for n in [2, 3, 5, 7, 11]:
        if not tmp%n:
            chk = True
            break
    if chk:
        print('YES')
    else:
        print('NO')