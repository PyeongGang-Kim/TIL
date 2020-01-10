import sys
input = sys.stdin.readline
def seg(s, e, idx = 1):
    if x <= s and e <= y:
        return nl[idx]
    if e < x or y < s:
        return 0
    m = (s + e) // 2
    return seg(s, m, idx << 1) + seg(m+1, e, (idx << 1) + 1)


N, Q = map(int, input().split())
N2 = 1
while N2 < N:
    N2 <<= 1
i = N2
N2 <<= 1
nl = [0 for _ in range(N2)]
for num in map(int, input().split()):
    nl[i] = num
    i += 1

tmp2 = (N2 >> 1) - 1
while tmp2:
    nl[tmp2] = nl[tmp2<<1] + nl[(tmp2<<1)+1]
    tmp2 -= 1

tmp2 = (N2 >> 1) - 1

chk = []
while Q:
    Q -= 1
    x, y, a, b = map(int, input().split())
    x -= 1
    y -= 1
    if x > y:
        x, y = y, x
    print(seg(0, tmp2))

    nl[a + tmp2] = b
    tmp3 = (a + tmp2) >> 1
    while tmp3:
        nl[tmp3] = nl[tmp3 << 1] + nl[(tmp3 << 1) + 1]
        tmp3 >>= 1
