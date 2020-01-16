i = 1
cl = [0] * 10100
while i < 10000:
    s = i
    t1, t2 = divmod(i, 10)
    while t1:
        s += t2
        t1, t2 = divmod(t1, 10)
    s += t2
    cl[s] = 1
    i += 1
i = 1
r = []
while i <= 10000:
    if not cl[i]:
        r.append(str(i))
    i += 1
print('\n'.join(r))