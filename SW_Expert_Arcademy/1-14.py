a=int(input())
cnt=0
for i in range(1,a+1):
        if 0==a%i:
         cnt=cnt+1
         print("%d(은)는 "%i+"%d의 약수입니다."%a)
if cnt==2:
    print("{}(은)는 1과 {}로만 나눌 수 있는 소수입니다.".format(a, a))