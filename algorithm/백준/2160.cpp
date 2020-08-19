#include <stdio.h>
char ml[50][5][8];
int N;
int cnt;
int res;
int result[2];
int main() {
	scanf("%d\n", &N);
	for (int k = 0; k < N; k++) {
		for (int j = 0; j < 5; j++) {
			scanf("%s", &ml[k][j]);
		}
	}
	res = 0xffffff;
	for (int j = 1; j < N; j++) {
		for (int i = 0; i < j; i++) {
			cnt = 0;
			for (int y = 0; y < 5; y++) {
				for (int x = 0; x < 7; x++) {
					if (ml[j][y][x] != ml[i][y][x]) cnt++;
				}
			}
			if (cnt < res) {
				res = cnt;
				result[0] = i;
				result[1] = j;
			}
		}
	}
	printf("%d %d\n", result[0]+1, result[1]+1);

	return 0;
}
