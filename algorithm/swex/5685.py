'''
단순 dfs로는 시간초과 발생한다.
dp 사용해야함.

'''

def solve(s, dep=1):
    global r, tmp
    if s < 0 or s > 20:
        return
    if dep == len(nl)-1:
        if nl[-1] == s:
            r += 1
        return
    solve(s+nl[dep], dep+1)
    solve(s-nl[dep], dep+1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    nl = list(map(int, input().split()))
    r = 0
    solve(nl[0])
    print(r)
