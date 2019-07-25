'''
방법 1.

a=input()
def palindrome(a):
    len_word=len(a)
    c=""
    for i in a:        
        c=i+c
    return c
d=str(palindrome(a))
print(d)
if a==d:
    print("입력하신 단어는 회문(Palindrome)입니다.")
'''

'''
방법 2.
a=input()
def palindrome(a):
    b=a[::-1]
    if a==b:
        return print('입력하신 단어는 회문(Palindrome)입니다.')
    else:
        return print('입력하신 단어는 회문(Palindrome)이 아닙니다.')
palindrome(a)
'''