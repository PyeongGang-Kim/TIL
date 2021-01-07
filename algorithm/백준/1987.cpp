#include <stdio.h>

int R, C;
char ml[20][21];
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };
int result = 0;

void dfs(int x, int y, int v, int c) {
	if (result < c) {
		result = c;
	}
	if (c == 26) return;
	int tx, ty, tv;

	for (int k = 0; k < 4; k++) {
		tx = x + dx[k];
		ty = y + dy[k];
		if (tx < C && -1 < tx && ty < R && -1 < ty) {
			if (!(v & (1 << ml[ty][tx]))) {
				tv = v | (1 << ml[ty][tx]);
				dfs(tx, ty, tv, c + 1);
			}
		}
	}
}


int main(void) {
	scanf("%d %d", &R, &C);
	for (int i = 0; i < R; i++) {
		scanf("%s", &ml[i]);
	}
	for (int j = 0; j < R; j++) for (int i = 0; i < C; i++) ml[j][i] -= 'A';
	dfs(0, 0, 1 << ml[0][0], 1);
	printf("%d", result);
	return 0;
}