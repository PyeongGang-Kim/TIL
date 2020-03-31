#include <stdio.h>
#include <queue>
#include <algorithm>
int N, M, S, T;
int a, b;
int t;
std::vector<int> ml[10001];
std::vector<int> ml2[10001];
int vl[10001] = { 0, };
int st[10001];
int st2[10001];
int stidx;
int stidx2;
int cl1[10001];
int cl2[10001] = { 0, };
int D[10001] = { 0, };
std::vector<std::vector<int> > Q;
// scc구조체
struct node {
	std::vector<int> next_node;
	int ind;
	int chk = 0;
	int num = 0;
} nl[10000];

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
	scanf("%d %d %d %d", &N, &M, &S, &T);
	while (M--) {
		scanf("%d %d", &a, &b);
		ml[a].push_back(b);
		ml2[b].push_back(a);
	}
	stidx = 0;
	for (int i = 1; i <= N; i++) {
		if (!vl[i]) {
			vl[i] = 1;
			dfs1(i);
		}
	}

	int cnum = 0;

	for (int i = 1; i <= N; i++) vl[i] = 0;
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

	for (int i = 1; i <= 10000; i++) vl[i] = 0;

	for (int i = 0; i < Q.size(); i++) {
		vl[i] = 1;
		for (int j = 0; j < Q[i].size(); j++) {
			for (int k = 0; k < ml[Q[i][j]].size(); k++) {
				if (!vl[cl1[ml[Q[i][j]][k]]]) {
					nl[i].next_node.push_back(cl1[ml[Q[i][j]][k]]);
					nl[cl1[ml[Q[i][j]][k]]].ind++;
					vl[cl1[ml[Q[i][j]][k]]] = 1;
				}
			}
		}
		for (int j = 0; j < nl[i].next_node.size(); j++) vl[nl[i].next_node[j]] = 0;
		vl[i] = 0;
	}
	int start = cl1[S];
	int end = cl1[T];
	int r;

	nl[start].chk = 1;
	// scc 위상정렬 수행
	for (int i = 1; i <= N; i++) vl[i] = 0;
	std::queue<int> Q2;
	for (int i = 0; i < Q.size(); i++) {
		if (!nl[i].ind) Q2.push(i);
	}
	int idx;
	while (!Q2.empty()) {
		idx = Q2.front();
		Q2.pop();
		for (int i = 0; i < nl[idx].next_node.size(); i++) {
			nl[nl[idx].next_node[i]].ind--;
			if (nl[idx].chk) {
				if (nl[nl[idx].next_node[i]].num < Q[idx].size() + nl[idx].num) {
					nl[nl[idx].next_node[i]].num = Q[idx].size() + nl[idx].num;
				}
				nl[nl[idx].next_node[i]].chk = 1;
			}
			if (!nl[nl[idx].next_node[i]].ind) {
				Q2.push(nl[idx].next_node[i]);
			}
		}
	}
	if (nl[end].chk) printf("%d", nl[cl1[T]].num + Q[cl1[T]].size());
	else printf("0");
	return 0;
}