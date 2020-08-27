#include <stdio.h>
#include <vector>
using namespace std;
char vl[1001] = { 0, };

vector<int> ml[1001];

void dfs(int i) {
	vl[i] = 1;
	for (int k = 0; k < ml[i].size(); k++) {
		if (!vl[ml[i][k]]) dfs(ml[i][k]);
	}
	return;
}
int main() {
	int N, M;
	scanf("%d %d", &N, &M);
	int u, v;

	while (M--) {
		scanf("%d %d", &u, &v);
		ml[u].push_back(v);
		ml[v].push_back(u);
	}
	int cnt = 0;

	for (int i = 1; i <= N; i++) {
		if (!vl[i]) {
			dfs(i);
			cnt++;
		}
	}
	printf("%d", cnt);
	return 0;
}
