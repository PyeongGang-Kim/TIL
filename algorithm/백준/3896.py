import sys
input = sys.stdin.readline
'''
if pl[i] 일 때 st에 i추가
이분탐색하면 더 빨리 할 수 있을 것 같다.
'''
pl = [1] * 1299710
pl[1] = 0
pl[0] = 0
i = 2
while i < 1142:
    if pl[i]:
        tmp = i ** 2
        while tmp < 1299710:
            pl[tmp] = 0
            tmp += i
    i += 1
i = 3
tmp = 2
while i < 1299710:
    if pl[i]:
        #pl[i] 인 곳까지 내려가면서
        #원하는 값 집어 넣기
        pre = i - 1
        tmp = i - tmp
        while not pl[pre]:
            pl[pre] = tmp
            pre -= 1
        pl[pre] = 0
        tmp = i
    i += 1
pl[-1] = 0
r = []
T = int(input())
while T:
    T -= 1
    r.append(str(pl[int(input())]))
print('\n'.join(r))