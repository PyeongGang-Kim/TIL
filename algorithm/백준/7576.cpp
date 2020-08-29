#include <stdio.h>
#include <queue>
int M, N;
char ml[1001][1000];
int main() {
	int cnt = 0;
	std::queue<std::pair<short, short>> q;
	scanf("%d %d", &M, &N);
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < M; i++) {
			scanf("%d", &ml[j][i]);
			if (!ml[j][i]) {
				cnt++;
			}
			else if (ml[j][i] == 1) {
				q.push({ i, j });
			}
		}
	}
	if (!cnt) {
		printf("0");
		return 0;
	}
	std::pair<short, short> tmp;
	short tx, ty;
	short dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 };
	int time = -1;
	int qsize;
	while (!q.empty()) {
		qsize = q.size();
		while (qsize--) {
			tmp = q.front();
			q.pop();
			for (int k = 0; k < 4; k++) {
				tx = tmp.first + dx[k];
				ty = tmp.second + dy[k];
				if (0 <= tx && M > tx && 0 <= ty && N > ty && ml[ty][tx] == 0) {
					ml[ty][tx] = 1;
					cnt--;
					q.push({ tx, ty });
				}
			}
		}
		time++;
	}
	if (cnt) {
		printf("-1");
	}
	else {
		printf("%d", time);
	}
	return 0;
}
