a=int(input())
b=[1,1,]
for i in range(2,a):
    b.append(b[i-2]+b[i-1])

print(b)
