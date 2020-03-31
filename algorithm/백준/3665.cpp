#include <stdio.h>
#include <queue>

int T, N, M;
int cnt[501];
int a, b, c;
int ml[501][501];
int nl[501];
int result[501];


int main(void) {
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j <= N; j++) {
				ml[i][j] = 0;
			}
			cnt[i] = 0;
		}
		for (int i = 0; i < N; i++) {
			scanf("%d", &nl[i]);
		}
		for (int i = 0; i < N-1; i++) {
			for (int j = i + 1; j < N; j++) {
				ml[nl[i]][nl[j]] = 1;
				cnt[nl[j]]++;
			}
		}
		scanf("%d", &M);
		while (M--) {
			scanf("%d %d", &a, &b);
			if (ml[a][b]) {
				cnt[b]--;
				cnt[a]++;
			}
			else {
				cnt[b]++;
				cnt[a]--;
			}
			ml[a][b] ^= 1;
			ml[b][a] ^= 1;
		}
		std::queue<int> Q;
		for (int i = 1; i <= N; i++) {
			if (!cnt[i]) {
				Q.push(i);
			}
		}
		int chk = 0;
		int idx = 0;
		while (!Q.empty()) {
			c = Q.front();
			if (Q.size() > 1) {
				chk = 1;
			}
			Q.pop();
			result[idx++] = c;
			for (int i = 1; i <= N; i++) {
				if (ml[c][i]) {
					if (!--cnt[i]) {
						Q.push(i);
					}
				}
			}
		}
		if (idx != N) {
			printf("IMPOSSIBLE\n");
		}
		else if (chk) {
			printf("?\n");
		}
		else {
			for (int i = 0; i < N; i++) {
				printf("%d ", result[i]);
			}
			printf("\n");
		}
	}
	return 0;
}