'''
dfs나 bfs를 사용하면 연산횟수가 nC0~nCn의 합이다.
삼각형의 크기가 500까지 생기므로 계산할 수가 없다.
따라서 동적계획법을 사용한다.
현재 위치의 값을 내 위의 왼쪽과 내 위 값중 큰 값을 비교해서 고르고 거기에 원래 있던 값을 더한 것으로 갱신한다.
이것을 맨 밑의 행까지 반복 후 맨 밑의 행에서 가장 최대값을 출력하면 된다.
'''



n = int(input())
nl = [[0] + list(map(int, input().split())) +[0] for _ in range(n)]
for i in range(1, n):
    for j in range(1, i+2):
        nl[i][j] += max(nl[i-1][j], nl[i-1][j-1])
print(max(nl[n-1]))