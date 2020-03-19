'''
문자열 하나씩 집어넣는다.
문자열 길이가 패턴보다 길 경우
현재 위치에서부터 패턴 길이만큼 되돌아가보면서 패턴과 일치하는지 확인한다.
터질 수 있는 문자열임이 확인 되면 idx를 문자열 길이만큼 줄인다.


idx위치에 다음 문자열을 집어넣는다
반복
'''


A = input()
B = input()
AB = len(A)-len(B)
li = [0]*len(A)
idx = 0
i = 0
while i < len(A):
    li[idx] = A[i]
    if idx >= len(B)-1:
        chk = False
        for j in range(len(B)):
            if li[idx-j] != B[len(B)-j-1]:
                chk = True
                break
        if not chk:
            idx -= len(B)

    i += 1
    idx += 1

r = []
if idx:
    for i in range(idx):
        r.append(li[i])
else:
    r = ['FRULA']
print(''.join(r))
