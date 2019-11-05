def perm(arr = []):
    if len(arr) == N:
        global result
        result.append(sorted(arr[:]))
        print(arr)
        return
    for i in range(len(nl)):
        arr.append(nl[i])
        perm(arr)
        arr.pop()


N = 3
nl = [1, 21, 3, 4, 5]
result = []
perm()
print(result)