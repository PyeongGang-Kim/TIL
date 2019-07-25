'''
방법 1.

a=[1, 2, 3, 4, 3, 2, 1]
print(a)
b=list(set(a))
print(b)
'''

'''
방법 2.
def cal(a):
    b=0
    for i in a:
        for k in range(b):
            if a[k]==a[b]:
                a.pop(b)
                cal(a)
                return a
        b+=1
               
a=[1, 2, 3, 4, 3, 2, 1]
print(a)
print(cal(a))
'''