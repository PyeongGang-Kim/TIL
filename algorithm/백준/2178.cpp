#include <stdio.h>
#include <queue>

int N, M;
char ml[100][101];
short vl[100][100];
struct pos {
	char x, y;
	short dis;
};

int main() {
	scanf("%d %d", &N, &M);
	for (int j = 0; j < N; j++) {
		scanf("%s", &ml[j]);
	}
	std::queue<pos> Q;
	Q.push({ 0, 0, 1 });
	pos tmp;
	char tx, ty;
	int dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 };
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < M; i++) vl[j][i] = 11111;
	}
	vl[0][0] = 1;
	while (!Q.empty()) {
		tmp = Q.front();
		Q.pop();
		if (tmp.x == M - 1 && tmp.y == N - 1) break;
		for (int i = 0; i < 4; i++) {
			tx = tmp.x + dx[i];
			ty = tmp.y + dy[i];
			if (0 <= tx && tx < M && 0 <= ty && ty < N) {
				if (ml[ty][tx] == '1' && vl[ty][tx] > tmp.dis + 1) {
					vl[ty][tx] = tmp.dis + 1;
					Q.push({ tx, ty, vl[ty][tx] });
				}

			}
		}
	}
	printf("%d", vl[N - 1][M - 1]);
	return 0;
}
