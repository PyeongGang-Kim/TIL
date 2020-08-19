#include <stdio.h>
char ml[1000][1000];
int N;
int pl[1000][1000];
int D[8][2] = { 0, -1, 1, -1, 1, 0, 1, 1, 0, 1, -1, 1, -1, 0, -1, -1};
int tx, ty;
int main() {
	scanf("%d\n", &N);
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			scanf("%c", &ml[j][i]);
			if (ml[j][i] > '0') {
				for (int k = 0; k < 8; k++) {
					tx = i + D[k][0];
					ty = j + D[k][1];
					if (0 <= tx && tx < N && 0 <= ty && ty < N) {
						pl[ty][tx] += ml[j][i] - '0';
					}
				}
			}
		}
		scanf("%c", &tx);
	}

	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			if (ml[j][i] > '0') printf("*");
			else if (pl[j][i] > 9) printf("M");
			else printf("%d", pl[j][i]);
		}
		printf("\n");
	}
	return 0;
}
