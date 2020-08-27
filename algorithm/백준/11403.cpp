#include <stdio.h>
int main() {
	int N;
	bool ml[101][101] = { 0, };
	scanf("%d", &N);
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			scanf("%d", &ml[j][i]);
		}
	}

	for (int k = 0; k < N; k++) {
		for (int j = 0; j < N; j++) {
			for (int i = 0; i < N; i++) {
				if (!ml[j][i] && ml[j][k] && ml[k][i]) {
					ml[j][i] = 1;

				}
			}
		}
	}

	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			printf("%d ", ml[j][i]);
		}
		printf("\n");
	}

	return 0;
}
