#include <stdio.h>
#include <queue>
#include <vector>

int T;
int K, M, P;
int cnt[1001][3];
int a, b;

std::vector<int> ml[1001];

int main(void) {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d %d", &K, &M, &P);
		for (int i = 1; i <= M; i++) {
			ml[i].clear();
			for (int k = 0; k < 3; k++) cnt[i][k] = 0;
		}

		while (P--) {
			scanf("%d %d", &a, &b);
			ml[a].push_back(b);
			cnt[b][0]++;
		}
		std::queue<int> Q;
		for (int i = 1; i <= M; i++) {
			if (!cnt[i][0]) {
				Q.push(i);
			}
		}

		int idx, tmp;
		while (!Q.empty()) {
			idx = Q.front();
			Q.pop();
			for (int j = 0; j < ml[idx].size(); j++) {
				tmp = ml[idx][j];
				cnt[tmp][0]--;
				if (cnt[idx][1] > cnt[tmp][1]) {
					cnt[tmp][1] = cnt[idx][1];
					cnt[tmp][2] = 1;
				}
				else if (cnt[idx][1] == cnt[tmp][1]) {
					cnt[tmp][2]++;
				}
				if (!cnt[tmp][0]) {
					if (cnt[tmp][2] > 1) {
						cnt[tmp][1]++;
					}
					Q.push(tmp);
				}
			}
		}
		printf("%d %d\n", tc, ++cnt[M][1]);
	}
	return 0;
}