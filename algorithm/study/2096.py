'''
다이나믹 프로그래밍
데이터를 전부 다 받고 난 다음 시작하면 메모리 초과가 난다.
데이터를 전부 다 받고 시작 할 필요는 없으므로 한 줄씩 받아오면서 계산을 수행하면 된다.

'''

import sys
N = int(input())
tl = list(map(int, sys.stdin.readline().split()))

tmax1, tmax2, tmax3 = tl
tmin1, tmin2, tmin3 = tl

for i in range(N-1):
    tl = list(map(int, sys.stdin.readline().split()))
    tmp1, tmp2, tmp3 = tmax1, tmax2, tmax3
    tmp1 = max(tmax1, tmax2) + tl[0]
    tmp2 = max(tmax1, tmax2, tmax3) + tl[1]
    tmp3 = max(tmax2, tmax3) + tl[2]
    tmax1, tmax2, tmax3  = tmp1, tmp2, tmp3

    tmp1, tmp2, tmp3 = tmin1, tmin2, tmin3
    tmp1 = min(tmin1, tmin2) + tl[0]
    tmp2 = min(tmin1, tmin2, tmin3) + tl[1]
    tmp3 = min(tmin2, tmin3) + tl[2]
    tmin1, tmin2, tmin3  = tmp1, tmp2, tmp3
print(max(tmax1, tmax2, tmax3), min(tmin1, tmin2, tmin3))