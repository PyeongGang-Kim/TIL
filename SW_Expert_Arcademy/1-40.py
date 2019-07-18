'''
방법 1.

def facto(a):
    b=1
    for i in range(2, a+1):
        b*=i
    return b
a=int(input())
print(facto(a))
'''


'''
방법 2.
def facto(a):
    if a==1:
        return 1
    b=1
    for i in range(2, a+1):
        b=a*facto(a-1)
    return b
a=int(input())
print(facto(a))
'''
