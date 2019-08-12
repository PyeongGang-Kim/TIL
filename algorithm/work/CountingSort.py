def counting_sort(A, B, k):
    # A 입력 숫자 리스트
    # B 정렬된 리스트
    # C 카운트 리스트
    C = [0] * k
    for i in range(0, len(B)):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]


a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0]*len(a)
counting_sort(a, b, 5)
print(b)