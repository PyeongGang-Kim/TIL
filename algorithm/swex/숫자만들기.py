def solve(s, dep=1):
    global rmin, rmax
    if dep == N:
        rmin = min(rmin, s)
        rmax = max(rmax, s)
        return
    for i in ra4:
        if ol[i]:
            ol[i] -= 1
            if i == 3 and nl[dep] != 0:
                solve(int(s/nl[dep]), dep+1)
            elif i == 0:
                solve(s+nl[dep], dep+1)
            elif i == 1:
                solve(s-nl[dep], dep+1)
            elif i == 2:
                solve(s*nl[dep], dep+1)
            ol[i] += 1

ra4 = range(4)

tc = int(input())

for t in range(1, tc+1):
    N = int(input())
    ol = list(map(int, input().split()))
    nl = list(map(int, input().split()))
    rmin = 100000000
    rmax = -100000000
    solve(nl[0])
    print('#%d %d' %(t, rmax-rmin))