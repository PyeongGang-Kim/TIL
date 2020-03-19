import sys
#sys.stdin = open('asdf.txt')
input = sys.stdin.readline
def seg(s, e, idx = 1):
    if b <= s and e <= c:
        return nl[idx]
    if e < b or c < s:
        return 0
    m = (s + e) // 2
    return seg(s, m, idx << 1) + seg(m+1, e, (idx << 1) + 1)


N, M = map(int, input().split())
N2 = 1
while N2 < N:
    N2 <<= 1
i = N2
N2 <<= 1
nl = [0 for _ in range(N2)]
tmp2 = (N2 >> 1) - 1
chk = []
while M:
    M -= 1
    a, b, c = map(int, input().split())
    if a == 1:
        nl[b+tmp2] += c
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
