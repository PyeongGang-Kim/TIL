import sys
input = sys.stdin.readline
def seg(s, e, su, idx = 1):
    if nl[idx] < su:
        return 1111111
    if s == e:
        return s + 1
    m = (s + e) // 2
    idx <<= 1
    if nl[idx] >= su:
        return seg(s, m, su, idx)
    else:
        return min(seg(s, m, su, idx), seg(m+1, e, su-nl[idx], idx + 1))


nl = [0] * 2097152
tmp = 1048575
r = []
n = int(input())
while n:
    n -= 1
    tmp2 = input()
    if tmp2[0] == '1':
        #꺼내기
        a, b = map(int, tmp2.split())
        #누적합이 b보다 작거나 같은 최대의 구간
        tmp3 = seg(0, tmp, b)
        idx = tmp + tmp3
        while idx:
            nl[idx] -= 1
            idx >>= 1
        r.append(str(tmp3))

    else:
        a, b, c = map(int, tmp2.split())
        # b맛 c개 넣기(b인덱스에 c 더하기)
        idx = tmp + b
        while idx:
            nl[idx] += c
            idx >>= 1


print('\n'.join(r))
