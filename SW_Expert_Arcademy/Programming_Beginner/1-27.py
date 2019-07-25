a=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
i=0
while i < len(a):
    if a[i]<80:
       a.pop(i)
       i-=1
    i=i+1
print(sum(a))