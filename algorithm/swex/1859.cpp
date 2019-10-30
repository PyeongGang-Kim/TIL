#include <stdio.h>
int T;
int N;
int nl[1000001];
int maxval;
long long result;
int main(void) {
	freopen("input.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		result = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &nl[i]);
		}
		maxval = -1;

		for (int i = N - 1; i >= 0; --i) {
			if (maxval < nl[i]) {
				maxval = nl[i];
			}
			else {
				result = result + maxval - nl[i];
			}
		}
		printf("#%d %lld\n", tc, result);
	}

}

