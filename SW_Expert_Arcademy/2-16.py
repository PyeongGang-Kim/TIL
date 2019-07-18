c=input().split(", ")
a=int(c[0])
b=int(c[1])
lis_a=[]
for i in range(a):
    lis_b=[]
    for k in range(b):
        lis_b.append(i*k)
    lis_a.append(lis_b)
print(lis_a)