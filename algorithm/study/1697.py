from collections import deque
'''
bfs
현재 위치에서 -1, +1, *2 이동한 좌표와 현재 cnt값의 +1한 값을 큐에 넣어준다.
도착지점(동생과 같은 경우) cnt를 반환하면 최소값이 나올 것임.

첫번째 가지치기 조건을 위해 tmp(set)를 사용한다.
똑같은 좌표에 도착했다면 이전에 도착한 것이 더 빠르기 때문에
늦게 도착한 좌표에 대해선 탐색할 필요가 없음.
방문할 때마다 tmp에 있는 값인지 확인 후 없으면 add해주고 큐에 삽입
있으면 그냥 넘어간다.

두번째 가지치기 조건. 현재 좌표가 동생보다 큰 값일 경우 +1과 *2로 갈 필요가 없다.
(간만큼 다시 -1씩 움직여 되돌아와야하기 때문)
세번째 가지치기 조건. 현재 좌표가 0보다 작아질 경우 -1로 갈 필요가 없다.
(*2 해봐야 음수로 커져 더 멀어지기 때문이다.)
'''
def bfs(p, cnt = 0):
    Q = deque([[p, cnt]])
    tmp.add(p)

    while Q:
        p, cnt = Q.popleft()
        if p == b:
            return cnt
        if p-1 not in tmp and p >= 0:
            tmp.add(p-1)
            Q.append([p-1, cnt+1])
        if p+1 not in tmp and p < b:
            tmp.add(p+1)
            Q.append([p+1, cnt+1])
        if p*2 not in tmp and p < b:
            tmp.add(p*2)
            Q.append([p*2, cnt+1])


a, b = map(int, input().split())
tmp = set()
print(bfs(a))