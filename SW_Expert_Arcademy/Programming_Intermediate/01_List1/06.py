a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int, input().split(" ")))
    print('#{} {}'.format(i+1,max(c)-min(c)))