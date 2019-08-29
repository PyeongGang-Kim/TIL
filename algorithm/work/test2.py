a=[1, 2, 3, 4]
b=[4, 5, 6, 7]
c=[6, 0, 9, 2]
nl = [[0 for _ in range(10)] for _ in range(10)]
s = []
s.append(a)
s.append(b)
s.append(c)
print(s)
for S in s:
    x1, y1, x2, y2 = S
    for j in range(y1, y2):
        for i in range(x1, x2):
            nl[j][i] = 1

for n in nl:
    print(n)
