import heapq
'''
최대 힙 + 최소 힙
최대 힙이 최소 힙보다 길이가 1 더 클경우
두 수 중 작은값을 최대 힙에 넣고 큰값을 최소 힙에 넣으면
최대힙의 루트가 우리가 찾는 중간값이 된다.

이 값들을 반복할때마다 더하고 20171109으로 나눈 나머지를 계산한다.
'''


T = int(input())
for t in range(1, T+1):
    N, tmp = map(int, input().split())
    sumn = 0
    a = []
    b = []
    heapq.heappush(a, -int(tmp))
    for _ in range(N):
        t1, t2 = map(int, input().split())
        if t1 >= t2:
            heapq.heappush(a, -t2)
            heapq.heappush(b, t1)
        else:
            heapq.heappush(a, -t1)
            heapq.heappush(b, t2)
        if -a[0] > b[0]:
            tmp1 = heapq.heappop(a)
            tmp2 = heapq.heappop(b)
            heapq.heappush(a, -tmp2)
            heapq.heappush(b, -tmp1)
        sumn = (sumn - a[0]) % 20171109

    print('#{} {}'.format(t, sumn))