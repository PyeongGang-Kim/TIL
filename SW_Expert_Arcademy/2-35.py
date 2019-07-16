a=input()
b=list(a)
c=sorted(list(set(a)))
for i in c:
    print(i+',%d'%b.count(i))