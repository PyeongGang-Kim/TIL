#include <stdio.h>
char ml[6][6] = { 0, };
char position[3];
char tx, ty;
char res = 1;
bool chk(char cx, char cy, char nx, char ny) {
	if (cx - nx == 2 || nx - cx == 2) {
		if (cy - ny == 1 || ny - cy == 1) return 1;
		return 0;
	}
	else if (cx - nx == 1 || nx - cx == 1) {
		if (cy - ny == 2 || ny - cy == 2) return 1;
		return 0;
	}
	return 0;
}

int main() {
	scanf("%s", &position);
	tx = position[1];
	ty = position[0];
	int cnt = 35;
	char initPosition[2];
	initPosition[0] = position[0];
	initPosition[1] = position[1];
	while (cnt--) {
		scanf("%s", &position);
		if (chk(tx, ty, position[1], position[0])) {
			if (ml[position[0] - 'A'][position[1] - '1']) {
				res = 0;
				break;
			}
			ml[position[0] - 'A'][position[1] - '1'] = 1;
		}
		else {
			res = 0;
			break;
		}
		tx = position[1];
		ty = position[0];
	}
	if (res && !ml[initPosition[1]][initPosition[0]]){
		if (chk(tx, ty, initPosition[1], initPosition[0])) {
			printf("Valid");
			return 0;
		}
	}
	printf("Invalid");
	return 0;
}
