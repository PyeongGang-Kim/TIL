def perm(idx):
    if idx == N:
        print(arr)
        return
    for i in range(idx, N):
        arr[i], arr[idx] = arr[idx], arr[i]
        perm(idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]
N = 4
arr = [1, 2, 3, 4]
perm(0)

