def solution(n):
    tmp = 0
    mystring = ''
    while n:
        n, tmp = divmod(n, 3)
        print("{} {}".format(n, tmp))
        mystring += str(tmp)
    answer = int(mystring, 3)
    return answer