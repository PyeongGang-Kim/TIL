b=[]
for i in range(1,11):
    b.append(i)
print(list(map(lambda x: x*x,list(filter(lambda x: x%2==0,b)))))