b=[1,1]
[b.append(b[i-1]+b[i]) for i in range(1,9)]
print(b)