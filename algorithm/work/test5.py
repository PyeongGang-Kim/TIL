import collections
q = collections.deque([1, 2,3, 4, 5])


tmp = 0
s= 5
tmp3 = 0
for i in range(len(q)):
    tmp += q[i]
    if tmp > s:
        break
tmp2 = len(q)
for _ in range(tmp2-i):
    tmp3 += q.pop()//2
print(q, tmp3)