def solve(dep = 0, s = 0):
    global R
    if dep >= 12:
        R = min(R, s)
        return
    if s > R:
        return
    #1일
    solve(dep+1, s + nl[dep] * vl[0])
    #1달
    solve(dep+1, s + vl[1])
    #3달
    solve(dep + 3, s + vl[2])


#1년이용권이랑 비교하기

T = int(input())
for t in range(1, T+1):
    vl = list(map(int, input().split()))
    nl = list(map(int, input().split()))
    R = vl[3]
    solve()
    print('#{} {}'.format(t, R))