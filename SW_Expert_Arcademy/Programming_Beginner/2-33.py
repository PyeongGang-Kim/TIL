a=list(input())
b=0
c=0
for i in a:
    if i.isalpha():
        if i.isupper():
            b+=1
        else:
            c+=1
print("UPPER CASE",b)
print("LOWER CASE",c)