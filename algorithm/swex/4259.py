'''
맨 마지막 수랑 그 앞의 수들로 분리한다.
그렇게 분리한 숫자들을 제곱연산을 해서 결과에 더해준다.
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = input().split()
    r = 0
    for n in nl:
        r += int(n[:-1])**int(n[-1])
    print('#{} {}'.format(t, r))