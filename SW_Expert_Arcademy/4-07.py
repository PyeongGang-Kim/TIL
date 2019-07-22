def find_page(l,r,c):
    cnt=0
    d=int((l+r)/2)
    while d!=c:
        if l<c<d:
            r=d
        else:
            l=d
        d=int((l+r)/2)
        cnt+=1
    return cnt

T=int(input())

for t in range(1,T+1):
    r, a, b = map(int, input().strip().split(' '))
    res_a=find_page(1, r, a)
    res_b=find_page(1, r, b)
    if res_a<res_b:
        print('#{} {}'.format(t, 'A'))
    elif res_a==res_b:
        print('#{} {}'.format(t, '0'))
    else:
        print('#{} {}'.format(t, 'B'))