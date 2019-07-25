a={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5}
b=list(a.keys())
c=list(a.values())

for i in range(len(a)):
    print("{}: {}".format(b[i],c[i]))