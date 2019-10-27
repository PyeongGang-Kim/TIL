from collections import deque
'''
bfs문제
N이 K보다 클 때를 생각해 줘야 함.
우선순위큐를 사용할 수도 있지만, 시간이 증가하지 않는 경우(순간이동)엔 그냥 appendleft를 활용해도 된다.
'''

N, K = map(int, input().split())
Q = deque()
vl = [False for _ in range(max(N, 2*K+2))]
Q.append([0, N])
while Q:
    tim, p = Q.popleft()
    if p == K:
        break
    if 0 < p < K:
        if not vl[p * 2]:
            Q.appendleft([tim, p * 2])
            vl[p * 2] = True
    if p > 0 and not vl[p-1]:
        Q.append([tim+1, p-1])
        vl[p-1] = True
    if p < K and not vl[p+1]:
        Q.append([tim+1, p+1])
        vl[p+1] = True

print(tim)