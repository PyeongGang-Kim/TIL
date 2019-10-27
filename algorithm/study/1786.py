'''
kmp 알고리즘

전처리 과정
현재 문자열의 위치 i와 패턴의 위치 j의 값이 같을 경우
i와 j를 각 각 1씩 더해준다.
다를 경우
j의 값을 P[j-1]로 갱신하면서 비교하다가 j가 0이 되어도 같지 않을 경우 i에 1을 더해준다.
같은 값이 나오면 P에 j+1값을 저장한 후 i와 j를 1씩 더해준다.

후처리 과정
현재 문자열의 위치 i와 패턴의 위치 j의 값이 같을 경우
i와 j를 각 각 1씩 더해준다.
다를 경우 j의 값을 P[j]로 갱신해 주고
j가 0이 된 경우 i의 값을 1 더해준다.
j의 길이가 패턴의 길이와 같아진 경우(패턴 전체와 같은 경우)
결과에 i-len(패턴)+1을 추가한다.
(i는 패턴 전체를 포함한 현재 위치이기때문에 시작점은 패턴의 길이만큼 빠져야 한다)

반복
'''


A = input()
B = input()
P = [0 for _ in range(len(B))]
r = []

for i in range(1, len(B)):
    while j > 0 and B[i] != B[j]:
        j = P[j-1]
    if B[i] == B[j]:
        j += 1
        P[i] = j

for i in range(len(A)):
    while j > 0 and B[j] != A[i]:
        j = P[j-1]
    if B[j] == A[i]:
        if j == len(B)-1:
            r.append(str(i+2-len(B)))
            j = P[j]
        else:
            j += 1
print(len(r))
print('\n'.join(r))