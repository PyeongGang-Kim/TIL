#include <stdio.h>
char bl[19][19];
char winner;
char dx[4] = {1, 1, 1, 0 };
char dy[4] = {-1, 0, 1, 1 };
char tx, ty;
char chk(int i, int j) {
	char tmp;
	if (bl[j][i]) {
		for (int p = 0; p < 4; p++) {
			tmp = 1;
			tx = i - dx[p];
			ty = j - dy[p];
			if (bl[j][i] == bl[ty][tx]) continue;

			for (int t = 1; t < 5; t++) {
				tx = i + dx[p] * t;
				ty = j + dy[p] * t;
				if (tx >= 0 && tx < 19 && ty >= 0 && ty < 19) {
					if (bl[j][i] == bl[j + dy[p] * t][i + dx[p] * t]) {
						tmp++;
					}
					else {
						break;
					}
				}
				else break;
			}
			if (tmp == 5){
				tx = i + dx[p] * 5;
				ty = j + dy[p] * 5;
				if (tx >= 0 && tx < 19 && ty >= 0 && ty < 19) {
					if (bl[j][i] != bl[ty][tx]) return bl[j][i];
				}
				else return bl[j][i];
			}
		}
	}
	return 0;
}

int main() {
	for (int j = 0; j < 19; j++) {
		for (int i = 0; i < 19; i++) {
			scanf("%d", &bl[j][i]);
		}
	}
	for (int j = 0; j < 19; j++) {
		for (int i = 0; i < 19; i++) {
			if (chk(i, j)) {
				printf("%d\n", bl[j][i]);
				printf("%d %d", j+1, i+1);
				return 0;
			}
		}
	}
	printf("0\n");
	return 0;
}
