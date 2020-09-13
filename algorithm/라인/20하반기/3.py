from collections import deque
def solution(n):
    if not n//10:
        return [0, n]
    # 숫자를 두 부분으로 나누면서 bfs 실행한다.
    q = deque([n])
    cnt = 0
    while q:
        qlen = len(q)
        cnt += 1
        while qlen:
            qlen -= 1
            n = q.popleft()
            if not n//10:
                return [cnt-1, n]
            nn = n
            k = 0
            while nn:
                nn //= 10
                k += 1
            for i in range(1, k):
                # 숫자를 나눠줄 위치 10**i
                tmp = 10**i
                if (n%tmp)//10**(i-1) or i == 1:
                    q.append((n//tmp) + (n%tmp))

print(solution(10007))
print(solution(73425))
print(solution(10000))