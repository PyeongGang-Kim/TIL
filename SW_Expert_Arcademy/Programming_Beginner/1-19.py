a=[str(i) for i in range(100,301)]
b=[]
for j in range(len(a)):
    chk=0
    for i in range(len(a[0])):
        if int(a[j][i])%2!=0:
            chk=1
            break
    if chk==0:
        b.append(a[j])

print(",".join(b))
