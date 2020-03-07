#include <stdio.h>
#include <queue>
#include <vector>

int N, M;
int cnt[101][2] = { 0, };
int vl[101];
int a, b, c;
std::vector<std::pair<int, int> > ml[101];

struct cmp {
	bool operator() (int a, int b) {
		return a > b;
	}
};

int main(void) {
	scanf("%d %d", &N, &M);
	while (M--) {
		scanf("%d %d %d", &a, &b, &c);
		ml[a].push_back({ b, c });
		cnt[b][0]++;
		vl[a] = 1;
	}
	cnt[N][1] = 1;
	std::queue<int> Q;
	Q.push(N);

	while (!Q.empty()) {
		a = Q.front();
		Q.pop();
		for (int i = 0; i < ml[a].size(); i++) {
			cnt[ml[a][i].first][1] += ml[a][i].second * cnt[a][1];
			if (!(--cnt[ml[a][i].first][0]))	Q.push(ml[a][i].first);
		}
	}
	for (int i = 1; i < N; i++) {
		if (!vl[i]) {
			printf("%d %d\n", i, cnt[i][1]);
		}
	}
	return 0;
}