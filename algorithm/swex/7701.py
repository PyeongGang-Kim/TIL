T = int(input())
for t in range(1, T+1):
    N = int(input())
    tmp = set()
    for _ in range(N):
        tmp.add(input())
    r = []
    for word in tmp:
        r.append([len(word), word])
    r.sort(key=lambda x: (x[0], x[1]))
    print('#%d' %t)
    for i, w in r:
        print(w)
