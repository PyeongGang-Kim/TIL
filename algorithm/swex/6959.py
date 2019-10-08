T = int(input())
for t in range(1, T+1):
    s = input()
    r = 0
    cnt = 0
    for num in s:
        r += int(num)
        cnt += 1
        if r//10:
            r -= 9
            cnt += 1
    if cnt&1:
        print('#{} B'.format(t))
    else:
        print('#{} A'.format(t))