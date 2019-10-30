#include <stdio.h>
int N = 10;
int T;
int r;
int tmp;

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		r = 0;
		for (int i = 0; i < N; ++i) {
			scanf("%d", &tmp);
			if (tmp & 1) {
				r = r + tmp;
			}
		}
		printf("#%d %d", tc, r);
	}
	
	return 0;

}