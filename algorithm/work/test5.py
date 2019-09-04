def chm(strnumber):
    strnumber = str(strnumber)
    if len(strnumber) == 1:
        return True
    for i in range(len(strnumber)-1):
        if strnumber[i] > strnumber[i+1]:
            return False
    return True


print(chm(9888))