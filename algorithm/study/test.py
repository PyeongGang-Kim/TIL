for test_case in range(1, 11):
    N = int(input())
    matric = [list(input()) for i in range(8)]
    trans_matric = list(zip(*matric))

    cnt = 0
    for i in range(len(matric)):
        for j in range(len(matric) - N + 1):
            a = matric[i][j: j + N]
            b = trans_matric[i][j: j + N]
            if a == a[::-1]:
                cnt += 1
            if b == b[::-1]:
                cnt += 1

    print('#{} {}'.format(test_case, cnt))