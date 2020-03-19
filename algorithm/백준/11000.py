'''
강의실 갯수가 힙의 원소 갯수.
강의실 중에서 가장 빨리 끝나는 강의실과
현재 강의장 비교
현재 강의장 시작 시간이 가장 빨리 끝나는 강의실보다 늦거나 같으면 해당 강의실에 들어간다.
그게 아니라면 그냥 강의장을 하나 더 추가한다
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())
nl = [list(map(int, input().split())) for _ in range(N)]
nl.sort()
Q = [nl[0][1]]
for i in range(1, N):
    if Q[0] <= nl[i][0]:
        heapq.heappushpop(Q, nl[i][1])
    else:
        heapq.heappush(Q, nl[i][1])
print(len(Q))