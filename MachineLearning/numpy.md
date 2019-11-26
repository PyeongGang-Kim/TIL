```python
mport numpy as np
# zeros: 세로 2 가로 2인 0으로만 채워진 2차원 배열
a = np.zeros((2,2))
print(a)
**# 출력:**
**# [[ 0. 0.]**
**# [ 0. 0.]]**

# ones: 세로 2 가로 3인 1로만 채워진 2차원 배열
a = np.ones((2,3))
print(a)
**# 출력:**
**# [[ 1. 1. 1.]**
**# [ 1. 1. 1.]]**

# full: 세로 2 가로 3인 원하는 값 5로만 채워진 2차원 배열
a = np.full((2,3), 5)
print(a)
**# 출력:**
**# [[5 5 5]**
**# [5 5 5]]**

# eye: 세로, 가로 3인 대각선만 1로 채워진 2차원 배열
a = np.eye(3)
print(a)
**# 출력:**
**# [[ 1. 0. 0.]**
**# [ 0. 1. 0.]**
**# [ 0. 0. 1.]]**

# 넘피 어레이 객체를 reshape하는 방법
# 길이 20짜리 배열을 세로 4 가로 5짜리 2차원 배열로 변경
# 갯수가 맞아야 함
a = np.array(range(20)).reshape((4,5))
print(a)
**# 출력:**
**# [[ 0 1 2 3 4]**
**# [ 5 6 7 8 9]**
**# [10 11 12 13 14]**
**# [15 16 17 18 19]]**

# 넘피배열을 슬라이싱
lst = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
arr = np.array(lst)
**# 슬라이스** 세로 0:2 가로 0:2 한 것
a = arr[0:2, 0:2]
print(a)
**# 출력:**
**# [[1 2]**
**# [4 5]]**

# 세로 1:, 가로 1: 한 것
a = arr[1:, 1:]
print(a)
**# 출력:**
**# [[5 6]**
**# [8 9]]**


# 정수 인덱싱
lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)
# 정수 인덱싱 [0][1], [2][3] 두개를 가져온다.
s = a[[0, 2], [1, 3]]
print(s)
# 출력
# [2 12]

# 참 불 인덱싱
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
# 방법 1. 똑같은 모양의 배열에 참 불 넣고 나서
# a[참불어레이]를 해 주면 된다.
bool_indexing_array = np.array([
    [False,  True, False],
    [True, False,  True],
    [False,  True, False]
])
n = a[bool_indexing_array];
print(n)    
# 방법 2. 논리연산을 사용
n = a[a%2==0]
print(n)
# %%%   a%2==0이 참 불 어레이를 만들어주기 때문에 동작하는 것임.

#넘피 배열끼리 더하기 빼기 곱하기 나누기를 시도하면 각 원소끼리 연산을 한다.
a = np.array([1,2,3])
b = np.array([4,5,6])
 
# 각 요소 더하기
c = a + b
# c = np.add(a, b)
print(c)  # [5 7 9]
 
# 각 요소 빼기
c = a - b
# c = np.subtract(a, b)
print(c)  # [-3 -3 -3]
 
# 각 요소 곱하기
# c = a * b
c = np.multiply(a, b)
print(c)  # [4 10 18]
 
# 각 요소 나누기
# c = a / b
c = np.divide(a, b)
print(c)  # [0.25 0.4 0.5]

# 행렬 곱 연산을 하려면 dot메서드를 이용한다. 2차원 초과하면 맨 마지막과 맨 마지막 앞의 것을 곱
# matmul도 있다. 약간 동작이 다르다. 2차원을 초과하면 2차원 배열을 여러개 갖고있다고 여김 맨 마지막 두개가 서로 곱할수 있어야 하며, 그 앞의 값이 두 행렬이 같아야한다.
# https://www.tutorialspoint.com/tensorflow/tensorflow_basics.htm
c = np.dot(a, b)

a = np.array([[1,2],[3,4]])
# axis를 입력하지 않으면 모든 요소들을 연산하여 하나로 만든다.
s = np.sum(a)
print(s)   # 10
# axis=0 이면, 0번축 방향으로 연산
# axis=1 이면, 1번축 방향으로 연산(각 축 방향이 생길 수 있는 모든 방식)
s = np.sum(a, axis=0)
print(s)   # [4 6]
s = np.sum(a, axis=1)
print(s)   # [3 7]
s = np.prod(a)
print(s)   # 24

# 좀 더 일반화 하면 shape가 (a, b, c) 인 넘피배열에서
# sum을 시도하면 axis=0일때 shape는 (b, c)
# axis=1일때 shape는 (a, c) 이런 방식.

```

