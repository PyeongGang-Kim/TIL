while 1:
    N = int(input())
    for i in range(N, 10000*N):
        tmp1 = int(''.join(reversed(list(str(i)))))
        if N == i-tmp1:
            print(i, tmp1, i-tmp1)
            break
        else:
            print(i, tmp1)
'''
N = input()
if len(N) & 1 and N[len(N) // 2] != '0':
# -1
else:
# 대칭으로 빼면서 최대값 따지기인데
# 마지막이 0 인 경우만 예외
'''