a=list(input())
cou=0
lenw=len(a)//2
for i in range(lenw):
    if a[i]==a[len(a)-1-i]:
        cou+=1
print(''.join(a))
if cou == lenw:
    print('입력하신 단어는 회문(Palindrome)입니다.')