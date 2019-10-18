def Stupid(arr):
    global r
    r += 1
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]


    else:
        m = len(arr) * 2 // 3
        for idx, n in enumerate(Stupid(arr[:m])):
            arr[idx] = n
        for idx, n in enumerate(Stupid(arr[len(arr)-m:])):
            arr[idx+len(arr)-m] = n
        for idx, n in enumerate(Stupid(arr[:m])):
            arr[idx] = n
    return arr


arr = [3, 2, 6, 1, 3, 2, 6, 8, 6, 8]
r = 0
Stupid(arr)
print(arr)
print(r)