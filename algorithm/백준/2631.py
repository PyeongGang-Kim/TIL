import sys
'''
최장 증가 부분 수열
dl[i]는 길이가 i인 값들 중 가장 작은 값을 갱신해 준다.
다음 값을 받았을 때 이 값이 맨 마지막 값보다 큰 값일 경우엔
dl을 이분탐색으로 탐색한다.

현재 값이 중앙값(인덱스)에 저장된 값보다 클 경우
그 중앙값+1에 저장된 값보다 작으면 중앙값+1에 현재 값을 입력
그게 아니면 이분탐색 진행

현재 값이 중앙값에 저장된 값보다 작을 경우
그 중앙값-1에 저장된 값보다 크면 중앙값에 현재 값을 입력
그게 아니면 이분탐색 진행

'''

def bs(c, front, rear):
    m = (front + rear) // 2
    if dl[m] < c:
        if dl[m+1] < c:
            bs(c, m, rear)
            return
        else:
            dl[m+1] = c
            return
    else:
        if dl[m-1] < c:
            dl[m] = c
        else:
            bs(c, front, m)
            return


N = int(sys.stdin.readline())
dl = [0 for _ in range(N+1)]
front, rear = 0, 1
i = 1
dl[1] = int(sys.stdin.readline())

while N > i:
    i += 1
    tmp = int(sys.stdin.readline())
    if dl[rear] < tmp:
        rear += 1
        dl[rear] = tmp
    else:
        bs(tmp, front, rear)

print(N - rear)