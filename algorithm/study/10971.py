'''
순열 한번 돌리고 모두 선택되었을 때 맨 마지막 요소에서 첫 시작점으로 이동거리를 더해서
그 결과값이 R보다 작을경우 R을 갱신한다.

순열돌리는 과정에서 현재 경로에 의한 거리값이 R보다 커질 경우 리턴한다.
선택될 수 있는지 매번 확인해 줘야 한다.

'''


def perm(k=0, s=0):
    global R
    if k == N:
        tmp = ml[arr[-1]][arr[0]]
        if tmp:
            R = min(R, tmp+s)
    if s > R:
        return

    for i in range(k, N):
        arr[i], arr[k] = arr[k], arr[i]
        tmp = ml[arr[k-1]][arr[k]]
        if k:
            if tmp:
                perm(k+1, s + tmp)
        else:
            perm(k+1, s)
        arr[i], arr[k] = arr[k], arr[i]


N = int(input())
ml = [list(map(int, input().split())) for _ in range(N)]
arr = [i for i in range(N)]
R = 1000000*12
perm()
print(R)