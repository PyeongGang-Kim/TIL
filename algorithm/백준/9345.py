import sys
input = sys.stdin.readline

'''
민맥스 세그
'''
def seg(s, e, idx=1):
    if b <= s and e <= c:
        if nl[idx][0] < b or nl[idx][1] > c:
            return False
        return True
    if c < s or b > e:
        return True
    m = (s + e) // 2
    idx <<= 1
    return seg(s, m, idx) and seg(m+1, e, idx+1)


r = []
nl = [[100001, -1] for _ in range(2 << 19)]
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
    i = 0
    while tmp < N2:
        if i < N:
            nl[tmp] = [i, i]
            i += 1
        tmp += 1
    tmp = offset
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
            if seg(0, default):
                r.append('YES')
            else:
                r.append('NO')
        else:
            # 바꿔끼우기
            b = b + offset
            c = c + offset
            nl[b], nl[c] = nl[c], nl[b]
            t1, t2 = b >> 1, c >> 1
            while t1:
                t3 = t1 << 1
                t4 = t3 + 1
                nl[t1][0] = min(nl[t3][0], nl[t4][0])
                nl[t1][1] = max(nl[t3][1], nl[t4][1])
                t1 >>= 1
            while t2:
                t3 = t2 << 1
                t4 = t3 + 1
                nl[t2][0] = min(nl[t3][0], nl[t4][0])
                nl[t2][1] = max(nl[t3][1], nl[t4][1])
                t2 >>= 1


print('\n'.join(r))
