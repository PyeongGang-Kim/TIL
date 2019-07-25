b=[]
for k in range(2,10):
    a = []
    for i in range(1,10):
        if (i*k)%3==0 or (i*k)%7==0:
            continue
        a.append(i*k)

    b.append(a)

print(b)