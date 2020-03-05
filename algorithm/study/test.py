T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cl = [0] * 10001
    nl = list(map(int, input().split()))
    tmp = [0]
    cl[0] = 1
    cnt = 1
    for k in range(N):
        for i in range(len(tmp)):
            tmp2 = tmp[i] + nl[k]
            if not cl[tmp2]:
                cl[tmp2] = 1
                tmp.append(tmp2)
                cnt += 1
    print('#{} {}'.format(tc, cnt))

