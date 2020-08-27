#include <stdio.h>
void lottop(char* lotto, char* lotto_a, int N, int idx, int dep=0) {
	if (dep == 6) {
		for (int i = 0; i < 6; i++) printf("%d ", lotto_a[i]);
		printf("\n");
		return;
	}
	if (idx == N) return;
	for (int i = idx; i < N; i++) {
		lotto_a[dep] = lotto[i];
		lottop(lotto, lotto_a, N, i + 1, dep + 1);
	}
	return;
}
int main() {
	char lotto[13];
	char lotto_a[6];
	int N;
	scanf("%d", &N);
	while (N) {
		for (int i = 0; i < N; i++) {
			scanf("%d", &lotto[i]);
		}
		lottop(lotto, lotto_a, N, 0);
		printf("\n");
		scanf("%d", &N);
	}


	return 0;
}
