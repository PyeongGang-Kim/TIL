#include <stdio.h>
#include <queue>
struct pos {
	char x, y, dir;
	int k;
};
char W, H;
char ml[100][101];
short vl[4][100][100];
char pt[4];
char* ptp;
int dep;

int dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 };

char cvt[2][4] = { 1, 0, 3, 2, 3, 2, 1, 0 };

int mkm(int cdep = 0, int i = 0) {
	std::queue<pos> Q;
	for (char k = 0; k < 4; k++) {
		Q.push({ pt[0], pt[1], k, 0});
	}
	int tim = 0;
	pos cp;
	short tk;
	char tx, ty, tdir;
	while (!Q.empty()) {
		int Qsize = Q.size();
		tim++;
		// 6, 0에서 세가지방향 5, 1에서 세가지방향

		while (Qsize--) {
			cp = Q.front(); Q.pop();
			tx = cp.x + dx[cp.dir];
			ty = cp.y + dy[cp.dir];
			tdir = cp.dir;
			tk = cp.k;
			if (0 <= tx && tx < W && 0 <= ty && ty < H && vl[tdir][ty][tx] > tk && ml[ty][tx] != '*') {
				vl[tdir][ty][tx] = tk;
				// 갈 수 있는 곳이면
				// 종료할수 있는 곳이면
				if (ml[ty][tx] == 'C' && ty == pt[3] && tx == pt[2]) {
					continue;
				}
				// 종료못하면 세가지경우의 수 넣는다.
				Q.push({ tx, ty, tdir, tk });
				Q.push({ tx, ty, cvt[0][tdir], tk + 1 });
				Q.push({ tx, ty, cvt[1][tdir], tk + 1 });
			}
		}
	}
	return -1;
}


int main() {
	scanf("%hhd %hhd", &W, &H);
	for (int j = 0; j < H; j++) scanf("%s", &ml[j]);
	ptp = pt;

	for (int j = 0; j < H; j++) for (int i = 0; i < W; i++) for (int k = 0; k < 4; k++) vl[k][j][i] = 30000;

	for (int j = 0; j < H; j++) for (int i = 0; i < W; i++) {
		if (ml[j][i] == 'C') {
			*ptp++ = i;
			*ptp++ = j;
		}
	}

	mkm();

	int res = 0xfffffff;
	for (int i = 0; i < 4; i++) {
		if (res > vl[i][pt[3]][pt[2]]) {
			res = vl[i][pt[3]][pt[2]];
		}
	}
	printf("%d", res);

	return 0;
}