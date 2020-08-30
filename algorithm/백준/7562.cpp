#include <stdio.h>
#include <algorithm>
#include <queue>
int dx[8] = { 1, 2, 2, 1, -1, -2, -2, -1 }, dy[8] = { -2, -1, 1, 2, 2, 1, -1, -2 };
int T, I;
bool nl[300][300];

int bfs() {
	int x, y, tx, ty;
	int time = 0;
	std::queue<std::pair<int, int>> q;
	scanf("%d %d %d %d", &x, &y, &tx, &ty);
	if (x == tx && y == ty) return time;
	nl[y][x] = 1;
	q.push({ x, y });
	std::pair<int, int> cp, np;
	while (!q.empty()) {
		int qsize = q.size();
		time++;
		while (qsize--) {
			cp = q.front(); q.pop();
			for (int k = 0; k < 8; k++) {
				np = { cp.first + dx[k], cp.second + dy[k] };
				if (0 <= np.first && np.first < I && 0 <= np.second && np.second < I && !nl[np.second][np.first]) {
					if (np.first == tx && np.second == ty) return time;
					nl[np.second][np.first] = 1;
					q.push(np);
				}
			}
		}
	}
	return -1;
}
int main() {
	scanf("%d", &T);
	int x, y, tx, ty;
	while (T--) {
		scanf("%d", &I);
		for (int j = 0; j < I; j++)for (int i = 0; i < I; i++)nl[j][i] = 0;
		printf("%d\n", bfs());
	}

	return 0;
}
