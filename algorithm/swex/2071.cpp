#include <stdio.h>
int T;
int nl[10];
int r1 = 0;
int tmp = 0;
int r;
int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		r1 = 0;
		for (int i = 0; i < 10; ++i) {
			scanf("%d", &tmp);
			r1 = r1 + tmp;

		}

		r = r1 / 10;
		if (r < int(r1 / 10.0 + 0.5)) {
			r += 1;
		}

		if (r < int(r1 / 10 +0.5)) {
			r = r + 1;
		}

		printf("#%d %d\n", tc, r);

	}
}