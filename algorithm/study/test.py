s = [i for i in range(100)]
s[9//2::3] = [0] * ((200 - 9 - 1) // 6 + 1)
print(s[9//2::3])
print(s)