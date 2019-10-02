'''
단속 카메라 각각의 좌표들을 셋에 담아 중복을 신경쓰지 않는다.
수신 영역이 카메라 갯수보다 많을 경우 수신영역은 0이 된다.
카메라 갯수가 많을 경우 (카메라 갯수 - 수신기 갯수)만큼
카메라 사이의 간격을 선택하면 된다.
카메라 사이의 간격들을 구하고 소팅해서 가장 작은 값들을 선택하면
수신영역이 최소화 되는 위치이다.
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    K = int(input())
    nl = set(map(int, input().split()))
    if len(nl) > K:
        nl = sorted(list(nl))
        dl = sorted([nl[i+1]-nl[i] for i in range(len(nl)-1)])
        tmp = 0
        for i in range(len(nl)-K):
            tmp += dl[i]
        r = tmp
    else:
        r = 0
    print('#{} {}'.format(t, r))
