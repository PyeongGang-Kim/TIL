#include <stdio.h>
int N;
char buf[20];
char U, LU_x, LU_y, V, LV_x, LV_y;
bool domino[8][9] = { 0, };
char sudoku_map[9][9] = { 0, };
int cnt = 1;
bool chkbox1[9][9] = { 0, };
bool chkbox2[9][9] = { 0, };
bool chkbox3[3][3][9] = { 0, };
int tx, ty;


bool check(int x, int y, int v) {
	if (!chkbox1[y][v] && !chkbox2[x][v] && !chkbox3[y / 3][x / 3][v]) return true;
	return false;
}

void fill(int x, int y, int v) {
	sudoku_map[y][x] = v + 1;
	chkbox1[y][v] = 1;
	chkbox2[x][v] = 1;
	chkbox3[y / 3][x / 3][v] = 1;
}
void fill2(int x, int y, int v) {
	sudoku_map[y][x] = 0;
	chkbox1[y][v] = 0;
	chkbox2[x][v] = 0;
	chkbox3[y / 3][x / 3][v] = 0;
}

bool solve(int p) {
	if (p == 81) {
		printf("Puzzle %d\n", cnt++);
		for (int j = 0; j < 9; j++) {
			for (int i = 0; i < 9; i++) {
				printf("%d", sudoku_map[j][i]);
			}
			printf("\n");
		}
		return true;
	}
	int x = p % 9;
	int y = p / 9;
	if (!sudoku_map[y][x]) {
		if (x + 1 < 9 && !sudoku_map[y][x + 1]) {
			for (int j = 0; j < 8; j++) for (int i = j + 1; i < 9; i++) {
				if (!domino[j][i]) {
					domino[j][i] = 1;
					if (check(x, y, j) && check(x + 1, y, i)) {
						fill(x, y, j);
						fill(x + 1, y, i);
						if (solve(p + 1)) return true;
						fill2(x, y, j);
						fill2(x + 1, y, i);
					}
					if (check(x, y, i) && check(x + 1, y, j)) {
						fill(x, y, i);
						fill(x + 1, y, j);
						if (solve(p + 1)) return true;
						fill2(x, y, i);
						fill2(x + 1, y, j);
					}
					domino[j][i] = 0;
				}
			}
		}
		if (y + 1 < 9 && !sudoku_map[y + 1][x]) {
			for (int j = 0; j < 8; j++) for (int i = j + 1; i < 9; i++) {
				if (!domino[j][i]) {
					domino[j][i] = 1;
					if (check(x, y, j) && check(x, y + 1, i)) {
						fill(x, y, j);
						fill(x, y + 1, i);
						if (solve(p + 1)) return true;
						fill2(x, y, j);
						fill2(x, y + 1, i);
					}
					if (check(x, y, i) && check(x, y + 1, j)) {
						fill(x, y, i);
						fill(x, y + 1, j);
						if (solve(p + 1)) return true;
						fill2(x, y, i);
						fill2(x, y + 1, j);
					}
					domino[j][i] = 0;
				}
			}
		}
	}
	else if (solve(p + 1)) return true;
	return false;
}
int main(void) {
	scanf("%d", &N);
	scanf("%c", &buf);
	while (N) {
		for (int j = 0; j < 8; j++) for (int i = 1; i < 9; i++) domino[j][i] = 0;
		for (int j = 0; j < 9; j++) for (int i = 0; i < 9; i++) {
			sudoku_map[j][i] = 0;
			chkbox1[j][i] = 0;
			chkbox2[j][i] = 0;
		}
		for (int k = 0; k < 3; k++) for (int j = 0; j < 3; j++) for (int i = 0; i < 9; i++) chkbox3[k][j][i] = 0;
		for (int i = 0; i < N; i++) {
			scanf("%[^\n]", &buf);
			U = buf[0] - '1';
			LU_y = buf[2] - 'A';
			LU_x = buf[3] - '1';
			V = buf[5] - '1';
			LV_y = buf[7] - 'A';
			LV_x = buf[8] - '1';
			if (U < V) domino[U][V] = 1;
			else domino[V][U] = 1;

			fill(LU_x, LU_y, U);
			fill(LV_x, LV_y, V);
			scanf("%c", &buf);
		}
		for (int j = 0; j < 9; j++) {
			scanf("%s", &buf);
			tx = buf[1] - '1';
			ty = buf[0] - 'A';

			fill(tx, ty, j);
		}
		solve(0);
		scanf("%d", &N);
		scanf("%c", &buf);
	}
	return 0;
}