tc = int(input())

for t in range(tc) :
    n = int(input())
    if n > 10 or n < 1:
        break
    print('#',t+1)
    pa = [[1],[1,1]]
    if n == 1:
        print(1)
    elif n == 2 :
        print(1)
        print('1 1')
    else :
        for i in range(2,n):
            i_list = [1]
            for j in range(i-1):
                i_list.append(pa[i-1][j]+pa[i-1][j+1])
            i_list.append(1)
            pa.append(i_list)
        for i in pa :
            for j in i:
                print(j, end=' ')
            print()