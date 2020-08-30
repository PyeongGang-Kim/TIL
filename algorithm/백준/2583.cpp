#include <stdio.h>
#include <algorithm>
#include <queue>
int M, N, K;
bool ml[100][100];
short res[5000];
int resp;
int dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 };

void bfs(int i, int j) {
	ml[j][i] = 1;
	std::queue<std::pair<int, int>> q;
	q.push({ i, j });
	std::pair<int, int> cp, np;
	int cnt = 1;
	while (!q.empty()) {
		cp = q.front();
		q.pop();
		for (int k = 0; k < 4; k++) {
			np = { cp.first + dx[k], cp.second + dy[k] };
			if (0 <= np.first && np.first < N && 0 <= np.second && np.second < M && !ml[np.second][np.first]) {
				cnt++;
				ml[np.second][np.first] = 1;
				q.push(np);
			}
		}
	}
	res[resp++] = cnt;
}
int main() {
	scanf("%d %d %d", &M, &N, &K);
	int x1, x2, y1, y2;

	while (K--) {
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		for (int j = y1; j < y2; j++) {
			for (int i = x1; i < x2; i++) ml[j][i] = 1;
		}
	}

	for (int j = 0; j < M; j++) {
		for (int i = 0; i < N; i++) {
			if (!ml[j][i]) bfs(i, j);
		}
	}

	std::sort(res, res + resp);
	printf("%d\n", resp);
	for (int i = 0; i < resp; i++) printf("%d ", res[i]);
	return 0;
}
