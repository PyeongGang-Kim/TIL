'''
단순한 문제이지만 고장난 버튼이 0 일 경우의 예외처리를 해 줘야함.
'''
N = int(input())
sn = str(N)
nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
if int(input()):
    tmp = set(input().split())
    nums = nums.difference(tmp)
n = 0
R = abs(N - 100)
nums = set(nums)
for i in range(N, -1, -1):
    tmn = str(i)
    chk = 0
    for tm in tmn:
        if tm not in nums:
            chk = 1
            break
    if not chk:
        tmp = N - i + len(str(i))
        if tmp < R:
            R = tmp
        break

for i in range(N, 1000001):
    tmn = str(i)
    chk = 0
    for tm in tmn:
        if tm not in nums:
            chk = 1
            break
    if not chk:
        tmp = i - N + len(str(i))
        if tmp < R:
            R = tmp
        break
print(R)