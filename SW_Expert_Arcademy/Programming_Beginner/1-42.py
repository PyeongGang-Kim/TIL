def fndlong(a):
    b=a.split(", ")

    if len(b[0])>len(b[1]):
        print(b[0])
        return
    else:
        print(b[1])
        return

a=input()
fndlong(a)