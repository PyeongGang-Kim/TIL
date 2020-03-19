'''
정렬을 한다.
하나씩 스택에 집어 넣는다
만약 맨 위 시간보다 더 늦게 시작하면 바로 넣는다
아닐 경우 더 빨리 끝나면 팝하고 넣는다
'''
import sys
input = sys.stdin.readline
N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]
nl.sort(key=lambda x: (x[1], x[0]))

r = nl[0]
cnt = 1
for i in range(1, N):
    if nl[i][0] >= r[1]:
        r = nl[i]
        cnt += 1
print(cnt)
