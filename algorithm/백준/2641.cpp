#include <stdio.h>
int N;
char sts[100];
char rsts[100];
char result[100][50];
int cnt;

bool chk2(char* ins) {
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			if (sts[i+j] != ins[i]) {
				break;
			}
			if (i == N - 1) {
				for (int k = 0; k < N; k++) result[cnt][k] = ins[k];
				cnt++;
				return 1;
			}
		}
	}

	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			if (rsts[i+j] != ins[i]) {
				break;
			}
			if (i == N - 1) {
				for (int k = 0; k < N; k++) result[cnt][k] = ins[k];
				cnt++;
				return 1;
			}
		}
	}
	return 0;
}
bool chk() {
	int M;
	scanf("%d", &M);
	char ins[50];
	char result = 0;
	while (M--) {
		for (int i = 0; i < N; i++) scanf("%d", &ins[i]);
		chk2(ins);
	}
	return 0;
}

int main() {
	scanf("%d ", &N);
	for (int i = 0; i < N; i++) {
		scanf("%d", &sts[i]);
	}
	for (int i = 0; i < N ; i++) {
		sts[i+N] = sts[i];
	}
	int j = 0;
	for (int i = 2 * N - 1; i>=0; i--) {
		rsts[j] = (sts[i] + 2)%4;
		if (!rsts[j]) rsts[j] = 4;
		j++;
	}
	chk();
	printf("%d\n", cnt);
	for (int i = 0; i < cnt; i++) {
		for (int k = 0; k < N-1; k++) {
			printf("%d ", result[i][k]);
		}
		printf("%d\n", result[i][N - 1]);
	}

	return 0;
}
