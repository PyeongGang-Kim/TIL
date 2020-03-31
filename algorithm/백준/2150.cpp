#include <stdio.h>
#include <queue>
#include<algorithm>

int st[10001];
std::vector<int> ml1[10001];
std::vector<int> ml2[10001];
int V, E, a, b;
int vl[10001] = { 0, };
int* stp = st;
int tmpsidx;
int tmps[10001];

struct cmp {
	bool operator() (std::vector<int> a, std::vector<int> b) {
		return a.front() > b.front();
	}
};
void dfs(int i) {
	for (int k = 0; k < ml1[i].size(); k++) {
		int j = ml1[i][k];
		if (!vl[j]) {
			vl[j] = 1;
			dfs(j);
		}
	}
	*stp = i;
	stp++;
	return;
}

void dfs2(int i) {
	for (int k = 0; k < ml2[i].size(); k++) {
		int j = ml2[i][k];
		if (!vl[j]) {
			vl[j] = 1;
			dfs2(j);
			tmps[tmpsidx++] = j;
		}
	}
	return;

}
int main(void) {
	scanf("%d %d", &V, &E);
	while (E--) {
		scanf("%d %d", &a, &b);
		ml1[a].push_back(b);
		ml2[b].push_back(a);
	}
	for (int i = 1; i <= V; i++) {
		if (!vl[i]) {
			vl[i] = 1;
			dfs(i);
		}
	}
	for (int i = 1; i <= V; i++) vl[i] = 0;

	std::priority_queue<std::vector<int>, std::vector<std::vector<int> >, cmp> Q;

	for (int i = V - 1; i >= 0; i--) {
		if (!vl[st[i]]) {
			vl[st[i]] = 1;
			tmpsidx = 1;
			tmps[0] = st[i];
			dfs2(st[i]);
			std::sort(tmps, tmps + tmpsidx);
			std::vector<int> tmp;
			for (int i = 0; i < tmpsidx; i++) {
				tmp.push_back(tmps[i]);
			}
			Q.push(tmp);
		}
	}
	printf("%d\n", Q.size());
	while (Q.size()) {
		for (int i = 0; i < Q.top().size(); i++) {
			printf("%d ", Q.top()[i]);
		}
		Q.pop();
		printf("-1\n");
	}
}