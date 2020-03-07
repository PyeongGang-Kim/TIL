#include <stdio.h>
#include <queue>
#include <vector>

int N, M;
int cnt[32001];
int a, b;
std::vector<int> ml[32001];

int main(void) {
	scanf("%d %d", &N, &M);
	while (M--) {
		scanf("%d %d", &a, &b);
		ml[a].push_back(b);
		cnt[b]++;
	}

	std::queue<int> Q;
	for (int i = 1; i <= N; i++) {
		if (!cnt[i]) {
			Q.push(i);
		}
	}

	int ridx = 0;

	while (!Q.empty()) {
		a = Q.front();
		Q.pop();
		printf("%d ", a);
		for (int i = 0; i < ml[a].size(); i++) {
			if (!(--cnt[ml[a][i]]))	Q.push(ml[a][i]);
		}
	}


	return 0;
}