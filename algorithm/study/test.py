i = 123

print(str(i * i)[-3:])
print(i*i)
for i in range(1000):
    if str(i*i)[-len(str(i)):] == str(i):
        print(i)