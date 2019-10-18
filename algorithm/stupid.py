def Stupid(s, e):
    global r
    r += 1
    if s+1 == e or s == e:
        if arr[s] > arr[e]:
            arr[s], arr[e] = arr[e], arr[s]
    else:
        m = s + (e - s) * 2 // 3
        Stupid(s, m)
        Stupid(e-m+s, e)
        Stupid(s, m)


arr = [3, 2, 6, 1, 3, 2, 6, 8, 6, 8]
r = 0
Stupid(0, len(arr)-1)
print(arr)
print(r)