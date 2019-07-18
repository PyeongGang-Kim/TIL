def findnum(a,b):
    d=False
    for i in range(len(a)):
        if a[i]==b:
            d=True
    return d
a=[2, 4, 6, 8, 10]
b=5
c=10
print(a)
print("{} => {}".format(b,findnum(a,b)))
print("{} => {}".format(c,findnum(a,c)))

