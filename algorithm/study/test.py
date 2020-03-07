
a = 1
b = 2
c = 3
# print(a^b, (a+b)&(!a&(b))

nl = [1, 2, 3, 2, 6, 346, 63,12, 17, 78, 84, 4, 1, 2345]
k = 0
for j in range(len(nl)-1):
    for i in range(j+1, len(nl)):
        k ^= nl[j] + nl[i]
print(k)
p = 0
for i in range(len(nl)):
    p ^= nl[i]

    if i & 1:
        p ^= nl[i]
print(p)
print(1^3^4^5^5^6^7^6^7^8^9^10^2^3^4)