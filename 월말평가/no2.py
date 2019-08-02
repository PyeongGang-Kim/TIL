'''
승연이는 간단한 사칙연산 문제지를 보관하다가 실수로 물을흘려서 숫자가 번졌다.
​
급하게 옮겨 적었지만 숫자를 알파벳으로 헷갈려 적어버렸다.
​
2는 2또는z, 5는 5또는s 0은0또는 알파벳o등으로 잘못 적었는데 원래의 수식으로 나타내라.
​
잘못 적은 영어 -> 환산시 숫자
​
lzmqsbyaqo -> 1234567890
​
'''
def transnum(trans_num):
    # 여기에 코드를 작성하시오.
    A = ['l','z','m','q','s','b','y','a','q','o']
    num = ''
    for i, j in enumerate(trans_num):
        if j in A:
            num += str(A.index(j)+1)
        else:
            num += j
    return(num)

if __name__ == '__main__':
    print(transnum('5m1z+1lz1')) #=> 5312+1121
    print(transnum('1zya*o')) #=> 1278*0
    print(transnum('q876-5432+123q')) #=> 9876-5432+123q
    print(transnum('43+10-s-11')) #=> 43+10-5-11