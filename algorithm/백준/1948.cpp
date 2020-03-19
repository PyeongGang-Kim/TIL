#include <stdio.h>
#include <queue>

int N, M;
int a, b, c;
long long cnt[10001] = { 0, };
int vl[10001] = { 0, };
std::vector<std::pair<int, int> > ml[10001];
std::vector<std::pair<int, int> > ml2[10001];

struct cmp {
	bool operator() (int a, int b) {
		return a > b;
	}
};
int s, e;
int main(void) {
	scanf("%d", &N);
	scanf("%d", &M);
	while (M--) {
		scanf("%d %d %d", &a, &b, &c);
		ml[a].push_back({ b, c });
		ml2[b].push_back({ a, c });
	}
	scanf("%d %d", &s, &e);
	std::priority_queue<int, std::vector<int>, cmp> Q;
	Q.push(s);
	cnt[s] = 0;
	int idx1;
	int idx2;
	int dis;
	while (!Q.empty()) {
		idx1 = Q.top();
		Q.pop();
		for (int i = 0; i < ml[idx1].size(); i++) {
			idx2 = ml[idx1][i].first;
			dis = ml[idx1][i].second;
			if (cnt[idx2] < cnt[idx1] + dis) {
				cnt[idx2] = cnt[idx1] + dis;
				Q.push(idx2);
			}
		}
	}

	std::queue<int> Q2;
	Q2.push(e);
	int ec = 0;
	while (!Q2.empty()) {
		idx1 = Q2.front();
		Q2.pop();
		for (int i = 0; i < ml2[idx1].size(); i++) {
			if (cnt[ml2[idx1][i].first] + ml2[idx1][i].second == cnt[idx1]) {
				if (!vl[ml2[idx1][i].first]) {
					vl[ml2[idx1][i].first] = 1;
					Q2.push(ml2[idx1][i].first);
				}
				ec++;
			}
		}
	}

	printf("%lld\n", cnt[e]);
	printf("%d\n", ec);

	return 0;
}