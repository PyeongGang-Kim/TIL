import sys
input = sys.stdin.readline
def bs(num, s, e):
    if s == e or s+1 == e:
        if st[s] < num:
            st[s+1] = num
        else:
            st[s] = num
        return
    m = (s + e)//2
    if num < st[m]:
        bs(num, s, m)
    elif st[m] < num:
        bs(num, m+1, e)


try:
    N = int(input())
    while N:
        nl = list(map(int, input().split()))
        st = [0]
        for num in nl:
            if num > st[-1]:
                st.append(num)
            elif st[-1] > num:
                bs(num, 0, len(st)-1)
        print(len(st)-1)
        N = int(input())
except:
    pass