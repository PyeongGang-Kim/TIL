a=int(input())
cnt=0
for i in range(1,a+1):
        if 0==a%i:
         cnt=cnt+1
         print("%d(은)는 "%i+"%d의 약수입니다."%a)