#include <stdio.h>
#include <algorithm>
char input_value[81];
bool chk1[9][10] = { 0, };
bool chk2[9][10] = { 0, };
bool chk3[3][3][10] = { 0, };


bool sudoku(int cur_p=0) {
	// 범위 넘어가면 리턴하기
	if (cur_p == 81) {
		// 출력 후 리턴 트루. 한번출력하면 끝내야하기 때문.
		int tmp_p = 0;
		for (int j = 0; j < 9; j++) {
			for (int i = 0; i < 9; i++) {
				printf("%d", input_value[tmp_p++]);
			}
			printf("\n");
		}
		return true;
	}

	int cur_x, cur_y, cur_bx, cur_by;
	if (input_value[cur_p]) {
		return sudoku(cur_p + 1);
	}
	else {
		cur_x = cur_p % 9;
		cur_y = cur_p / 9;
		cur_bx = cur_x / 3;
		cur_by = cur_y / 3;
		for (int i = 1; i < 10; i++) {
			if (!chk1[cur_x][i] && !chk2[cur_y][i] && !chk3[cur_by][cur_bx][i]) {
				chk1[cur_x][i] = 1;
				chk2[cur_y][i] = 1;
				chk3[cur_by][cur_bx][i] = 1;
				input_value[cur_p] = i;
				if (sudoku(cur_p + 1)) return true;
				chk1[cur_x][i] = 0;
				chk2[cur_y][i] = 0;
				chk3[cur_by][cur_bx][i] = 0;
				input_value[cur_p] = 0;
			}
		}
	}
	return 0;
}
int main(void) {
	char tmp;

	int cur_x, cur_y, cur_bx, cur_by;
	for (int i = 0; i < 81; i++) {

		scanf("%c", &tmp);
		while (tmp < 11) {
			scanf("%c", &tmp);
		}

		cur_x = i % 9;
		cur_y = i / 9;
		cur_bx = cur_x / 3;
		cur_by = cur_y / 3;
		tmp -= '0';
		input_value[i] = tmp;
		chk1[cur_x][tmp] = 1;
		chk2[cur_y][tmp] = 1;
		chk3[cur_by][cur_bx][tmp] = 1;
	}
	sudoku();
	return 0;

}