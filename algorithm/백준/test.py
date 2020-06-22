li = [0, 1, 2, 3, 4]
for idx in range(3):
    for i in range(len(li)):
        if li[i] == idx:
            li.pop(i)
            print(li)
            break