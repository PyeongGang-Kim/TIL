'''
세그먼트 트리 사용해서 풀이하였으나 이정도로 할 필요는 없음.

그냥 인덱스 i에는 i까지의 합을 저장해놓고
i1, i2까지 합을
D[i2] - D[i1]을 하면 된다.


세그먼트 트리 사용 시 탐색의 범위보다 큰 최소의 2의 N승만큼의 범위를 잡는다.
범위가 14일 경우 16(2**4) 범위가 5일 경우 8(2**3) 등
그 범위만큼의

'''

def sumt(l, r, s=1, e=2**20, idx=1):
    if e < l or s > r:
        return 0
    if l <= s and e <= r:
        return D[idx]
    m = (s+e)//2
    return sumt(l, r, s, m, idx*2) + sumt(l, r, m+1, e, idx*2+1)


D = [0 for _ in range(2**20)]
for i in range(1, 2**20, 2):
    for j in range(i, 2**20, i):
        D[j] += i
D = [0 for _ in range(2**20-1)] + D
for i in range(2**21-2, 1, -1):
    D[i//2] += D[i]

T = int(input())
for t in range(1, T+1):
    L, R = map(int, input().split())
    print('#{} {}'.format(t, sumt(L, R)))