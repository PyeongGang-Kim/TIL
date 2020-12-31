def perm(arr, i=0):
    if i == len(arr):
        print(arr)
    for idx in range(i, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(arr, i+1)
        arr[idx], arr[i] = arr[i], arr[idx]
    return


arr = [1, 2, 3, 5, 6]
perm(arr)