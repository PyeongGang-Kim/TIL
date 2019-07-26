def ppp(a):
    if len(a)<=1:
        return len(a)
    chk=0
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            a.pop(i-1)
            a.pop(i-1)
            ppp(a)
            break

    return len(a)
T=int(input())

for t in range(1,T+1):
    a=list(input())
    result=ppp(a)

    print('#{} {}'.format(t, result))