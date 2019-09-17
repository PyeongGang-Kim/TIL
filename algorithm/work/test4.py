import sys
sys.stdin = open('asdf.txt')


N = 10
A = [0]*N
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printSet(n):
    for i in range(n):
        if A[i] == 1:
            print("%d " % data[i], end='')
    print()

def powerset(n, k):
    if n == k:
        tmp = 0
        for i in range(len(data)):
            tmp += A[i]*data[i]
        if tmp == 10:
            printSet(n)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

powerset(N, 0)