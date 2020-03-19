import sys
input = sys.stdin.readline
def seg(s, e, idx = 1):
    if b <= s and e <= c:
        return nl[idx]
    if s <= b <= e or s <= c <= e:
        m = (s + e) // 2
        return seg(s, m, idx << 1) + seg(m+1, e, (idx << 1) + 1)
    return 0


N, M, K = map(int, input().split())
N2 = 1
while N2 < N:
    N2 <<= 1
i = N2
N2 <<= 1
nl = [0 for _ in range(N2)]
tmp = i + N
while i < tmp:
    nl[i] = int(input())
    i += 1
tmp = M + K
tmp2 = (N2 >> 1) - 1
chk = []
while tmp2:
    nl[tmp2] = nl[tmp2 << 1] + nl[(tmp2 << 1) + 1]
    tmp2 -= 1
tmp2 = (N2 >> 1) - 1


while tmp:
    tmp -= 1
    a, b, c = map(int, input().split())
    if a == 1:
        nl[b+tmp2] = c
        chk.append(b+tmp2)
    else:
        b -= 1
        c -= 1
        for num in chk:
            tmp3 = num >> 1
            while tmp3:
                nl[tmp3] = nl[tmp3 << 1] + nl[(tmp3 << 1) + 1]
                tmp3 >>= 1
        chk = []
        print(seg(0, tmp2))