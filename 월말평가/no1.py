'''
교열이는 특별한 숫자를 비밀번호로 만들려고 하는데 각 숫자를 자릿수길이로 제곱을 하여 더했을때 일치하면 비밀번호로 정하려고 한다.
​
숫자를 넣었을때 비밀번호로 타당한지에 대한 함수를 만들어라 
​
ex) 153 -> 3자리의 숫자
​
1^3 + 5^3 + 3^3 = 153(일치)
​
1634 -> 4자리의 숫자
​
1^4 + 6^4 + 3^4 + 4^4 = 1634(일치)
'''
def pass_word(pass_word):
    # 여기에 코드를 작성하시오.
    return sum([int(s)**len(pass_word) for s in pass_word])==int(pass_word)

if __name__ == '__main__':
    print(pass_word('7')) #=> True
    print(pass_word('153')) #=> True
    print(pass_word('84')) #=> False
    print(pass_word('1634')) #=> True