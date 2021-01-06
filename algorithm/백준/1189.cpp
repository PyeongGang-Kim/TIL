/*
시작점과 도착점이 같아지는 경우가 있을 수 있는 조건이므로 이를 고려해야 한다.
*/

#include <stdio.h>
char R, C, K;
bool vl[6][6] = { 0, };
char nl[6][7];
int D[2][4] = { 0, 1, 0, -1, -1, 0, 1, 0 };
// 각 위치에서 도착점까지의 최단거리가 원하는 거리 초과할경우 리턴하기.
int dfs(int x, int y, int dis = 1) {
	if (R - x + y + dis > K) return 0;

	if (y == 0 && x == C) {
		// 도착점이므로 K와 비교한다.
		if (nl[y][x] == 'T') return 0;
		if (dis == K) return 1;
		return 0;
	}
	int cnt = 0;
	char tx, ty;
	for (int i = 0; i < 4; i++) {
		tx = x + D[0][i];
		ty = y + D[1][i];
		if (-1 < tx && tx <= C && -1 < ty && ty <= R && !vl[ty][tx]) {
			vl[ty][tx] = 1;
			cnt += dfs(tx, ty, dis + 1);
			vl[ty][tx] = 0;
		}
	}
	return cnt;
}
int main(void) {
	scanf("%hhd %hhd %hhd", &R, &C, &K);
	char tmp;
	for (char j = 0; j < R; j++) scanf("%s", &nl[j]);

	for (char j = 0; j < R; j++) for (char i = 0; i < C; i++) {
		if (nl[j][i] != '.') vl[j][i] = 1;
	}
	R--;
	C--;
	vl[R][0] = 1;
	R&& C ? printf("%d", dfs(0, R)) : printf("1");
	return 0;
}