def summary(word):
    result = []
    tmp_list = []

    for char in word:
        if tmp_list and tmp_list[-1] != char:
            result.append(tmp_list[-1])
            result.append(f'{len(tmp_list)}')
            tmp_list.clear()
        tmp_list.append(char)
    

print(summary('aabbaacc'))
#a2b2a2c2
print(summary('ffgggeeeef'))
#f2g3e4f1
print(summary('abcdefg'))
#a1b1c1d1e1f1g1