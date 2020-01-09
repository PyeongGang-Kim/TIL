from collections import deque
Q = deque()
sorted(Q)

a = [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]

a.sort(key=lambda x: x[1])

print(a)