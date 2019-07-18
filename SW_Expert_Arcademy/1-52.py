def largr(*a):
    c=0
    b=[]
    for i in a[0]:
        b.append(i)
    return max(b)


a=(3,5,4,1,8,10,2)
b=largr(a)
print("max{} => {}".format(a,b))
