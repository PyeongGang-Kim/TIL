#include <stdio.h>
char ml[12][12] = { 0, };
char D[2][4] = { 0, 1, 0, -1, -1, 0, 1, 0 };

int main() {
	int R, C, cnt;
	char tmp;
	scanf("%d %d\n", &R, &C);
	//scanf("%c", &tmp);

	for (int j = 1; j <= R; j++) {
		for (int i = 1; i <= C; i++) {
			scanf("%c", &tmp);
			if (tmp == '.') ml[j][i] = 1;
		}
		scanf("%c", &tmp);
	}

	for (int j = 1; j <= R; j++) {
		for (int i = 1; i <= C; i++) {
			cnt = 0;
			if (ml[j][i]) {
				for (int k = 0; k < 4; k++) {
					if (ml[j + D[1][k]][i + D[0][k]]) cnt++;
				}
				if (cnt < 2) {
					printf("1");
					return 0;
				}

			}
		}
	}
	printf("0");

	return 0;
}
