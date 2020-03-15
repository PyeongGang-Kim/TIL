//실패
// 사이클들을 구하고 각 사이클들을 유니온파인드로 이어주면서 진행
#include <stdio.h>
#include <queue>
#include <algorithm>
int n, m;
int a, b;
int t;
std::vector<int> ml[301];
std::vector<int> ml2[301];
int vl[301];
int st[301];
int st2[301];
int stidx;
int stidx2;
int result[600];
int ridx;
int cl1[301];
int cl2[301];

int findset(int i) {
	if (cl2[i]) {
		cl2[i] = findset(cl2[i]);
		return cl2[i];
	}
	return i;
}
void init() {
	for (int i = 1; i <= n; i++) {
		vl[i] = 0;
		ml[i].clear();
		ml2[i].clear();
		cl2[i] = 0;
	}
	ridx = 0;
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
	char tmp[301];
	while (t--) {
		scanf("%d", &n);
		init();

		for (int j = 1; j <= n; j++) {
			scanf("%s", &tmp);
			for (int i = 0; i < n; i++) {
				if (tmp[i] == '1') {
					ml[j].push_back(i + 1);
					ml2[i + 1].push_back(j);
				}
			}
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
				stidx2--;
				for (int i = 0; i < stidx2; i++) {
					tq.push_back(st2[i]);
					result[ridx++] = st2[i];
					result[ridx++] = st2[i+1];
					cl1[st2[i]] = cnum;
				}
				tq.push_back(st2[stidx2]);
				cl1[st2[stidx2]] = cnum++;
				if (stidx2) {
					result[ridx++] = st2[stidx2];
					result[ridx++] = st2[0];
				}
				Q.push_back(tq);
			}
		}

		int t1, t2;

		for (int i = 0; i < Q.size(); i++) {
			for (int j = 0; j < Q[i].size(); j++) {
				t1 = findset(cl1[Q[i][j]]);
				for (int k = 0; k < ml[Q[i][j]].size(); k++) {
					t2 = findset(cl1[ml[Q[i][j]][k]]);
					if (t1 != t2) {
						cl2[t2] = t1;
						result[ridx++] = Q[i][j];
						result[ridx++] = ml[Q[i][j]][k];
					}
				}
			}
		}

		printf("%d\n", ridx >> 1);
		for (int i = 0; i < ridx >> 1; i++) {
			printf("%d %d\n", result[2 * i], result[2 * i + 1]);
		}
		printf("\n");
	}
}