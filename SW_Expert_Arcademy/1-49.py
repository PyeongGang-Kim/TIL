b=[]
for i in range(1,11):
    b.append(i)
print(list(filter(lambda x: x%2==0,b)))
