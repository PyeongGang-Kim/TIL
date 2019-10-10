def solve(s, arr=[0, 0, 0, 0], cnt = 1):
    if cnt == len(ol):
        print(s)
        return
    for i in range(4):
        if arr[i] <= ol[i]:
            arr[i] += 1
            cnt += 1
            if i == 0:
                solve(s+nl[cnt], arr, cnt)
            elif i == 1:
                solve(s-nl[cnt], arr, cnt)
            elif i == 2:
                solve(s*nl[cnt], arr, cnt)
            elif i == 3:
                solve(s//nl[cnt], arr, cnt)
            arr[i] -= 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ol = list(map(int, input().split()))
    nl = list(map(int, input().split()))
    solve(nl[0])