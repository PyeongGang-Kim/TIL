T = int(input())
for t in range(1, T+1):
    N = int(input())
    sum_num = (N//2+N%2)*(-1)**(N%2+1)
    print('#{} {}'.format(t, sum_num))
