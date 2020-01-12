import sys
import math




nl = [i & 1 for i in range(123457)]
nl[1] = 0
nl[2] = 1
st = [2]
sqn = int(math.sqrt(123456)) + 1
num = 3
while num < 123457:
    if nl[num]:
        st.append(num)
        tmp = num ** 2
        while tmp < 123457:
            if nl[tmp]:
                nl[tmp] = 0
                st.append(tmp)
            tmp += num
    num += 2
st.sort()
D = [0] * 123457 * 2
i = 2
i2 = 1
while i < 123457 * 2:
    D[i] = i2
    if st[i2] == i:
        i2 += 1
        if i2 == len(st):
            break
    i += 1

a = int(input())

while a:
    cnt = 0
    i = D[a]
    a *= 2
    while st[i] <= a:
        if st[i]:
            cnt += 1
        i += 1
    print(cnt)
    a = int(input())
print()