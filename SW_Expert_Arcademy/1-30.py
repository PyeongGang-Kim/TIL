a=input()
b=[0 for i in range(10)]
for i in range(10):
    for n in a:
        if i==int(n):
            b[i]+=1
b=list(map(str,b))
print('0 1 2 3 4 5 6 7 8 9')
print(" ".join(b))