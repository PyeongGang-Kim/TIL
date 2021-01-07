#include <stdio.h>
int N;
double h[4];
bool vl[30][30] = { 0, };
double res = 0.0;
char D[2][4] = { 1, -1, 0, 0, 0, 0, 1, -1 };

void dfs(double cur_h = 1.0, int x = 14, int y = 14, int dep = 0) {
	// 재방문 없이 횟수 다 한 경우..
	if (dep == N) {
		res += cur_h;
		return;
	}

	int tx, ty;
	for (int d = 0; d < 4; d++) {
		tx = x + D[0][d];
		ty = y + D[1][d];
		if (!vl[ty][tx]) {
			vl[ty][tx] = 1;

			dfs(cur_h * h[d], tx, ty, dep + 1);
			vl[ty][tx] = 0;
		}
	}

}
int main(void) {
	int tmp;
	scanf("%d", &N);
	for (int t = 0; t < 4; t++) {
		scanf("%d", &tmp);
		h[t] = tmp / 100.0;
	}
	vl[14][14] = 1;
	dfs();
	printf("%.10lf\n", res);
	return 0;

}