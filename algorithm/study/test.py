import sys
input = sys.stdin.readline

'''
민맥스 세그
'''
def seg(b, c, s, e, idx=1):
    if b <= s and e <= c:
        if nl[idx][0] < b or nl[idx][1] > c:
            return False
        return True
    if c < s or b > e:
        return True
    m = (s + e) // 2
    idx <<= 1
    return seg(b, c, s, m, idx) and seg(b, c, m+1, e, idx+1)


r = []
T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    N2 = 2
    while N2 < N:
        N2 <<= 1
    offset = N2
    N2 <<= 1
    tmp = offset
    nl = [[100001, -1] for _ in range(offset)] + [[i, i] for i in range(N)] + [[100001, -1] for _ in range(offset-N)]
    i = 0
    while tmp:
        tmp -= 1
        tmp2 = tmp << 1
        nl[tmp][0] = min(nl[tmp2][0], nl[tmp2+1][0])
        nl[tmp][1] = max(nl[tmp2][1], nl[tmp2+1][1])

    default = offset - 1

    while M:
        M -= 1
        a, b, c = map(int, input().split())
        if a:
            # 구간 확인하기
            r.append('YES' if seg(b, c, 0, default) else 'NO')
        else:
            # 바꿔끼우기
            b = b + offset
            c = c + offset
            nl[b], nl[c] = nl[c], nl[b]
            for t1 in b >> 1, c >> 1:
                while t1:
                    t3 = t1 << 1
                    t4 = t3 + 1
                    nl[t1][0] = min(nl[t3][0], nl[t4][0])
                    nl[t1][1] = max(nl[t3][1], nl[t4][1])
                    t1 >>= 1


print('\n'.join(r))
