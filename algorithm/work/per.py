def per(visit, arr=[], d = 1):
    global nl
    if d > len(visit):
        result.append(arr[:])
        return
    for i in range(len(nl)):
        if visit[i] == 0:
            arr.append(nl[i])
            visit[i] = 1
            per(visit, arr, d + 1)
            arr.pop()
            visit[i] = 0



nl = [1, 2, 3]
visit = [0 for i in nl]
result = []
per(visit)
print(result)