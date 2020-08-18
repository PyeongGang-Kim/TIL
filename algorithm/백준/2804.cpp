#include <stdio.h>
char A[31], B[31];
int cnt[100];
int a, b;
char D[31][31];
int main() {
	scanf("%s", &A);
	scanf("%s", &B);
	for (int i = 0; B[i]; i++) {
		if (!cnt[B[i]]) cnt[B[i]] = i + 1;
	}
	for (int i = 0; A[i]; i++) {
		if (cnt[A[i]]) {
			a = cnt[A[i]] - 1;
			b = i;
			break;
		}
	}

	for (int j = 0; B[j]; j++) {
		for (int i = 0; A[i]; i++) {
			if (i == b) {
				D[j][i] = B[j];
			}
			else if (j == a) {
				D[j][i] = A[i];
			}
			else D[j][i] = '.';
		}
	}

	for (int j = 0; B[j]; j++) {
		printf("%s\n", D[j]);
	}

	return 0;
}
