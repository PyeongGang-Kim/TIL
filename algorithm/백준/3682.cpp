#include <stdio.h>
#include <queue>
#include <algorithm>
int n, m;
int a, b;
int t;
std::vector<int> ml[20001];
std::vector<int> ml2[20001];
int vl[20001];
int st[20001];
int st2[20001];
int stidx;
int stidx2;
int cl1[20001];
int cl2[20001];
int cl3[20001];

void init() {
	for (int i = 1; i <= n; i++) {
		vl[i] = 0;
		ml[i].clear();
		ml2[i].clear();
		cl2[i] = 0;
		cl3[i] = 0;
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
	scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &n, &m);
		init();
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

		int cnum = 1;
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
					cl1[st2[i]] = cnum;
				}
				cnum++;
				Q.push_back(tq);
			}
		}

		int t1, t2;

		for (int i = 0; i < Q.size(); i++) {
			for (int j = 0; j < Q[i].size(); j++) {
				// 시작점과 도착점 cnum이 다를경우 cl2도착점 cnum위치에 ++, cl3시작점 cnum위치에 ++
				// Q[i][j] 가 시작점이다. ml[Q[i][j]][k] 가 도착점이다.
				for (int k = 0; k < ml[Q[i][j]].size(); k++) {
					if (cl1[Q[i][j]] != cl1[ml[Q[i][j]][k]]) {
						cl2[cl1[ml[Q[i][j]][k]]]++;
						cl3[cl1[Q[i][j]]]++;
					}
				}
			}
		}
		int cnt1 = 0;
		int cnt2 = 0;

		if (Q.size() == 1) {
			printf("0\n");
		}
		else {
			for (int i = 1; i <= Q.size(); i++) {
				if (!cl2[i]) cnt1++;
				if (!cl3[i]) cnt2++;
			}
			printf("%d\n", cnt1 > cnt2 ? cnt1 : cnt2);
		}
	}
}