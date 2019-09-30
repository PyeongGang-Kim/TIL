'''
가장 높은 가치를 뽑아내야 한다.
가장 높은 가치 3개 묶으면 그중 가장 작은값(3번째로 비싼 값)을 빼고
그 다음 남은 물건들 중에서 가장 높은 가치 3개를 묶고 그중 가장 작은 값(6번째로 비싼 값)을 뺀다
반복
'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = sorted(list(map(int, input().split())), reverse=True)
    i = 2
    R = sum(nl)
    while len(nl) > i:
        R -= nl[i]
        i += 3
    print('#{} {}'.format(t, R))

