fruit = ['   apple    ','banana','  melon']
for i in range(len(fruit)):
    fruit[i]=fruit[i].strip()
d={n:len(n) for n in fruit}
print(d)