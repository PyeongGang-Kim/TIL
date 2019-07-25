def prod(*a):
    b=1
    for i in a:
        if type(i)!=int:
            return print("에러발생")
        b*=i
    return print(b)

prod(1,2,'4',3)