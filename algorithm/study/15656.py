'''
중복순열 출력하기

중복순열 출력을 위해선 인풋 리스트에 중복이 없어야 하므로
set을 사용해 중복을 줄인다.
작은 수부터 출력을 위해 정렬을 한다.
'''
def perm(arr = []):
    if len(arr) == M:
        print(' '.join(arr))
        return
    for i in range(len(nl)):
        arr.append(str(nl[i]))
        perm(arr)
        arr.pop()

N, M = map(int, input().split())
nl = sorted(list(set(map(int, input().split()))))
perm()