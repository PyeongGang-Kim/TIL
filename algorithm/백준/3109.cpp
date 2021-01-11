#include <stdio.h>
int R, C;
char ml[10000][501];
int res = 0;


// dfs 리턴 후 방문배열 초기화를 하지 않아도 답에 영향이 없으며,
// 애초에 다음번째 방문시에도 불가능한 위치이므로 방문하지 말 것.
bool dfs(int x, int y) {
	if (x == C - 1) {
		res++; return true;
	}
	if (y-1 > -1 && ml[y-1][x+1] == '.') {
		ml[y - 1][x + 1] = 'O';
		if (dfs(x + 1, y - 1)) return true;
	}
	if (ml[y][x + 1] == '.') {
		ml[y][x + 1] = '0';
		if (dfs(x + 1, y)) return true;
	}
	if (y + 1 < R && ml[y + 1][x + 1] == '.') {
		ml[y + 1][x + 1] = '0';
		if (dfs(x + 1, y + 1)) return true;
	}
	return false;
}


int main(void) {
	scanf("%d %d", &R, &C);
	for (int j = 0; j < R; j++) scanf("%s", &ml[j]);
	for (int i = 0; i < R; i++) dfs(0, i);
	printf("%d", res);
	return 0;
}