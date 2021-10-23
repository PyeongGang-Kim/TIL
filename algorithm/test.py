def per(dep):
    if dep == len(a):
        print(a)
        return

    for i in range(dep, len(a)):
        a[i], a[dep] = a[dep], a[i]
        per(dep+1)
        a[i], a[dep] = a[dep], a[i]

def comb(dep, arr = []):
    if dep == len(a):
        print(arr)
        return
    comb(dep+1, arr)
    arr.append(a[dep])
    comb(dep+1, arr)
    arr.pop()



a = [1, 2, 3, 4, 5]
# per(0)
comb(0)

