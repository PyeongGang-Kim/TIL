#include <stdio.h>

int T;
int N, M;
int s, e, c;
int ml[401][401];
int inf = 0xFFFFFFF;
int tmp;
int main(void) {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &N, &M);
		for (int j = 1; j <= N; j++) {
			for (int i = 1; i <= N; i++) {
				ml[j][i] = inf;
			}
		}
		while (M--) {
			scanf("%d %d %d", &s, &e, &c);
			ml[s][e] = c;
		}
		for (int k = 1; k <= N; k++) {
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (ml[i][k] + ml[k][j] < ml[i][j]) {
						ml[i][j] = ml[i][k] + ml[k][j];
					}
				}
			}
		}
		int r = inf;

		for (int i = 1; i <= N; i++) {
			if (r > ml[i][i]) {
				r = ml[i][i];
			}
		}
		if (r == inf) {
			printf("#%d %d\n", tc, -1);
		}
		else {
			printf("#%d %d\n", tc, r);
		}
	}
	return 0;
}