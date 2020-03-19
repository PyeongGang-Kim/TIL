#include <stdio.h>
#include <queue>
#include <vector>

int N, M;
int cnt[1001];
int num;
int a, b;
int tmp[1001];
short result[1001];
std::vector<int> ml[1001];

int main(void) {
	scanf("%d %d", &N, &M);
	while (M--) {
		scanf("%d", &num);
		for (int i = 0; i < num; i++) {
			scanf("%d", &tmp[i]);
		}

		for (int i = 1; i < num; i++) {
			ml[tmp[i - 1]].push_back(tmp[i]);
			cnt[tmp[i]]++;
		}
	}

	std::queue<int> Q;
	for (int i = 1; i <= N; i++) {
		if (!cnt[i]) {
			Q.push(i);
		}
	}

	short ridx = 0;
	while (!Q.empty()) {
		a = Q.front();
		Q.pop();
		result[ridx++] = a;
		for (int i = 0; i < ml[a].size(); i++) {
			cnt[ml[a][i]]--;
			if (!cnt[ml[a][i]]) {
				Q.push(ml[a][i]);
			}
		}
	}
	if (ridx != N) {
		printf("0");
	}
	else for (int i = 0; i < N; i++) printf("%d\n", result[i]);
	return 0;
}