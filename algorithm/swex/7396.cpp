#include <stdio.h>
#include <queue>

int T;
int N, M;
char ml[2001][2001];
int vl[2001][2001];
char chk;
int x, y;
char a;
char result[4000];
int idx;
struct pos {
	int x, y;
	char a;
}cp, np;
struct cmp {
	bool operator()(pos a, pos b) {
		return b.a < a.a;
	}
};

int main(void) {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &N, &M);
		for (int j = 0; j < N; j++) {
			scanf("%s", &ml[j]);
		}
		idx = 0;
		for (int j = 0; j < N; j++) {
			for (int i = 0; i < M; i++) {
				vl[j][i] = 0;
			}
	}
		std::priority_queue<pos, std::vector<pos>, cmp> Q;
		cp.x = 0;
		cp.y = 0;
		cp.a = ml[0][0];
		Q.push(cp);
		chk = ml[0][0];
		while (!Q.empty()){
			a = Q.top().a;
			result[idx++] = a;
			std::priority_queue<pos, std::vector<pos>, cmp> tmp;
			while (!Q.empty() && Q.top().a == a) {
				cp = Q.top();
				Q.pop();
				if (cp.y < N-1) {
					np.x = cp.x;
					np.y = cp.y + 1;
					if (!vl[np.y][np.x]) {
						vl[np.y][np.x] = 1;
						np.a = ml[np.y][np.x];
						tmp.push(np);
					}
				}
				if (cp.x < M - 1) {
					np.x = cp.x + 1;
					np.y = cp.y;
					if (!vl[np.y][np.x]) {
						vl[np.y][np.x] = 1;
						np.a = ml[np.y][np.x];
						tmp.push(np);
					}
				}
			}
			Q = tmp;
		}
		result[idx] = '\0';
		printf("#%d %s\n", tc, result);
	}
	return 0;
}