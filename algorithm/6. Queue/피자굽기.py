import sys
sys.stdin = open('피자굽기.txt')


def inp():
    idx = 1
    while pl:
        if not SN[0][1]:
            SN.pop(0)
            SN.append([idx, pl.pop(0)])
            idx += 1
        else:
            return idx
    return idx


def fp():
    idx = inp()
    cnt = 0
    while 1:
        if SN[0][1]:
            SN[0][1] //= 2
            if SN[0][1]:
                P = SN[0][0]
                SN.append(SN.pop(0))
                cnt = 0
            else:
                cnt += 1
        else:
            if pl:
                SN[0] = [idx, pl.pop(0)]
                idx += 1
                cnt = 0
                P = SN[0][0]
            else:
                SN.append(SN.pop(0))
                cnt += 1
        if cnt > N+1:
            break
    return P


results = []
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    pl = list(map(int, input().split()))
    SN = [[0, 0] for _ in range(N)]
    inx = 1
    results.append('#{} {}'.format(t, fp()))
print('\n'.join(results))