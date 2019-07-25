a=[12,24,35,24,88,120,155,88,120,155]
i=0
while i<len(a):
    k=i+1
    while k<len(a):
        if a[i]==a[k]:
            a.pop(k)
            k-=1
        k+=1
    i+=1
print(a)
