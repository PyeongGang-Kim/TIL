a=int(input())
i=1
b=''
while a>=2**i:
    i+=1
i=i-1
b=str(a//(2**i))
while i>0:
    a=a%(2**i)
    i-=1
    b+=str(a//(2**i))
print(b)
