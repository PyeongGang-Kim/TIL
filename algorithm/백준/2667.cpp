#include <stdio.h>
#include <queue>
#include <vector>
#include <algorithm>
int N;
char ml[25][26];
char vl[25][25];
char dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 };
std::queue<std::pair<short, short>> q;
std::vector<short> res;

void bfs(char i, char j) {
	vl[j][i] = 1;
	q.push({ i, j });

	char tx, ty;
	short cnt = 1;
	char x, y;
	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for (int k = 0; k < 4; k++) {
			tx = x + dx[k];
			ty = y + dy[k];
			if (0 <= tx && tx < N && 0 <= ty && ty < N && ml[ty][tx] == '1' && !vl[ty][tx]) {
				vl[ty][tx] = 1;
				q.push({ tx, ty });
				cnt++;
			}
		}

	}
	res.push_back(cnt);
}

int main() {
	scanf("%d", &N);
	for (int j = 0; j < N; j++) {
		scanf("%s", &ml[j]);
	}

	for (char j = 0; j < N; j++) {
		for (char i = 0; i < N; i++) {
			if (ml[j][i] == '1' && !vl[j][i]) {
				bfs(i, j);
			}
		}
	}
	std::sort(res.begin(), res.end());
	printf("%d\n", res.size());
	for (int i = 0; i < res.size(); i++) printf("%d\n", res[i]);

	return 0;
}
