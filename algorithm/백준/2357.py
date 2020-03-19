import sys
input = sys.stdin.readline
def seg(s, e, idx = 1):
    if a <= s and e <= b:
        return nl[idx]
    if s <= a <= e or s <= b <= e:
        m = (s + e) // 2
        t1, t2 = seg(s, m, idx << 1)
        t3, t4 = seg(m+1, e, (idx << 1) + 1)
        return min(t1, t3), max(t2, t4)
    return 1000000000, 1


N, M = map(int, input().split())
N2 = 1
while N2 < N:
    N2 <<= 1
i = N2
N2 <<= 1
nl = [[1000000000, 1] for _ in range(N2)]
tmp = i + N
while i < tmp:
    nl[i][0] = int(input())
    nl[i][1] = nl[i][0]
    i += 1
tmp2 = (N2 >> 1) - 1
while tmp2:
    nl[tmp2][0] = min(nl[tmp2 << 1][0], nl[(tmp2 << 1) + 1][0])
    nl[tmp2][1] = max(nl[tmp2 << 1][1], nl[(tmp2 << 1) + 1][1])
    tmp2 -= 1
tmp2 = (N2 >> 1) - 1
tmp = M
while tmp:
    tmp -= 1
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(*seg(0, tmp2))