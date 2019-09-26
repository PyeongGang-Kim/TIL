def comb(dep = 0):
    if len(arr) == n:
        print(arr)
        return
    if dep == len(a):
        return
    arr.append(a[dep])
    comb(dep+1)
    arr.pop()
    comb(dep+1)

arr = []

a = [1, 2, 3, 4, 5]
n = 4
comb()