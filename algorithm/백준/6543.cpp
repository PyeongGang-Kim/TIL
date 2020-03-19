#include <stdio.h>
#include <queue>
#include <algorithm>
int n, m;
int a, b;
std::vector<int> ml[5001];
std::vector<int> ml2[5001];
int vl[5001];
int st[5001];
int st2[5001];
int stidx;
int stidx2;
void init() {
	for (int i = 1; i <= n; i++) {
		vl[i] = 0;
		ml[i].clear();
		ml2[i].clear();
	}
}

void dfs1(int i) {
	for (int j = 0; j < ml[i].size(); j++) {
		if (!vl[ml[i][j]]) {
			vl[ml[i][j]] = 1;
			dfs1(ml[i][j]);
		}
	}
	st[stidx++] = i;
}

void dfs2(int i) {
	for (int j = 0; j < ml2[i].size(); j++) {
		if (!vl[ml2[i][j]]) {
			vl[ml2[i][j]] = 1;
			dfs2(ml2[i][j]);
		}
	}
	st2[stidx2++] = i;
}

int main(void) {
	scanf("%d", &n);
	while (n) {
		init();
		scanf("%d", &m);
		while (m--) {
			scanf("%d %d", &a, &b);
			ml[a].push_back(b);
			ml2[b].push_back(a);
		}

		stidx = 0;
		for (int i = 1; i <= n; i++) {
			if (!vl[i]) {
				vl[i] = 1;
				dfs1(i);
			}
		}

		std::vector<std::vector<int> > Q;
		for (int i = 1; i <= n; i++) vl[i] = 0;
		while (stidx--) {
			if (!vl[st[stidx]]) {
				vl[st[stidx]] = 1;
				stidx2 = 0;
				dfs2(st[stidx]);
				std::vector<int> tq;
				for (int i = 0; i < stidx2; i++) {
					tq.push_back(st2[i]);
				}
				Q.push_back(tq);
			}
		}
		stidx = 0;

		for (int i = 1; i <= n; i++) vl[i] = 0;
		for (int i = 0; i < Q.size(); i++) {
			for (int j = 0; j < Q[i].size(); j++) {
				vl[Q[i][j]] = 1;
			}
			int chk = 0;
			for (int j = 0; j < Q[i].size(); j++) {
				for (int k = 0; k < ml[Q[i][j]].size(); k++) {
					if (!vl[ml[Q[i][j]][k]]) {
						chk = 1;
						break;
					}
				}
			}
			if (!chk) {
				for (int j = 0; j < Q[i].size(); j++) {
					st[stidx++] = Q[i][j];
				}
			}
		}

		std::sort(st, st + stidx);
		for (int i = 0; i < stidx; i++) printf("%d ", st[i]);
		printf("\n");

		scanf("%d", &n);
	}
}