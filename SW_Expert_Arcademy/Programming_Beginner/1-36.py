def cal_prime(n):
    if n==1:
        return 1
    b=0

    for i in range(2,n):
        if n%i==0:
            b+=1
    if b==0:
        n=0
    else:
        n=1
    return n
a=int(input())
d=cal_prime(a)
if d==0:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")