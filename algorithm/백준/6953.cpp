#include <stdio.h>
#include <queue>
char L, R, C;
char ml[30][30][31];
// 상 하 좌 우 앞 뒤
char dx[6] = { 0, 0, -1, 1, 0, 0 }, dy[6] = { 0, 0, 0, 0, -1, 1 }, dz[6] = { -1, 1, 0, 0, 0, 0 };

struct pos {
	char x, y, z;
};

char sx, sy, sz;
int time = 0;

bool bfs() {
	std::queue<pos> q;
	q.push({ sx, sy, sz });
	pos cp, np;
	while (!q.empty()) {
		int qsize = q.size();
		time++;
		while (qsize--) {
			cp = q.front(); q.pop();
			for (char k = 0; k < 6; k++) {
				np = { cp.x + dx[k], cp.y + dy[k], cp.z + dz[k] };
				if (0 <= np.x && np.x < C && 0 <= np.y && np.y < R && 0 <= np.z && np.z < L) {
					if (ml[np.z][np.y][np.x] == 'E') {
						return 1;
					}
					else if (ml[np.z][np.y][np.x] == '.') {
						ml[np.z][np.y][np.x] = '#';
						q.push(np);
					}
				}
			}
		}
	}
	return 0;
}

int main() {
	scanf("%hhd %hhd %hhd", &L, &R, &C);
	while (L) {
		time = 0;
		for (int i = 0; i < L; i++) {
			for (int j = 0; j < R; j++) scanf("%s", &ml[i][j]);
		}
		for (char k = 0; k < L; k++) for (char j = 0; j < R; j++) for (char i = 0; i < C; i++) {
			if (ml[k][j][i] == 'S') {
				sx = i;
				sy = j;
				sz = k;
			}
		}


		if (bfs()) printf("Escaped in %d minute(s).\n", time);
		else printf("Trapped!\n");
		scanf("%hhd %hhd %hhd", &L, &R, &C);
	}

	return 0;
}