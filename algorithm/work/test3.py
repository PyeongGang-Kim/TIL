import sys
sys.stdin = open('asdf.txt')


T = int(input())
for t in range(1, T+1):
    N, C = map(int, input().split())
    nl = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1]/x[0],reverse=True)
    tmp = 0
    for i in range(len(nl)):
        if C * nl[i][1] / 100 > nl[i][0]:
            C = C * (100 - nl[i][1]) / 100
            tmp += nl[i][0]
        else:
            break

    print('#{} {}'.format(t, C+tmp))