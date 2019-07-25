def square(a):

    b=a.split(", ")
    for i in range(len(b)):
        print("square({}) => {}".format(int(b[i]),int(b[i])*int(b[i])))

    return

a=input()
square(a)
