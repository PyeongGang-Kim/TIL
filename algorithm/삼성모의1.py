def rot(arr):
    return [[arr[j][i] for j in range(len(arr)-1, -1, -1)] for i in range(len(arr[0]))]


def chk(x, y, arr):
    global cnt
    for j in range(len(arr)):
        for i in range(len(arr[0])):
            if arr[j][i] and nl[j+y][i+x]:
                return False

    for j in range(len(arr)):
        for i in range(len(arr[0])):
            if arr[j][i]:
                nl[j+y][i+x] = 1
                cnt += 1
    return True


def solve(arr):
    # 5*5일때 3*4가 들어오면 y 2번 x 3번
    for j in range(N-len(arr) + 1):
        for i in range(M - len(arr[0]) + 1):
            if chk(i, j, arr):
                return True
    return False


N, M, K = map(int, input().split())
nl = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0
while K:
    R, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    for n in range(4):
        if solve(arr):
            break
        if n != 3:
            arr = rot(arr)
    K -= 1
print(cnt)