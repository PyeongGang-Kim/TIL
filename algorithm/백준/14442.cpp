#include <stdio.h>
#include <queue>
short N, M;
char K;
char ml[1000][1001];
char vl[1000][1000];
char dx[4] = { -1, 1, 0, 0 }, dy[4] = { 0, 0, -1, 1 };
struct pos {
	short x, y;
	char k;
};

int main() {
	scanf("%hd %hd %hhd", &N, &M, &K);
	for (int j = 0; j < N; j++) scanf("%s", &ml[j]);
	std::queue<pos> q;
	q.push({ 0, 0, K+1 });
	int time = 0;
	if (N == 1 && M == 1) {
		printf("1");
	}
	else {
		pos cp, np;
		vl[0][0] = K+1;
		while (!q.empty()) {
			time++;
			int qsize = q.size();
			while (qsize--) {
				cp = q.front(); q.pop();
				if (cp.x == M - 1 && cp.y == N - 1) {
					printf("%d", time);
					return 0;
				}
				for (int k = 0; k < 4; k++) {
					np = { cp.x + dx[k], cp.y + dy[k], cp.k };
					if (0 <= np.x && np.x < M && 0 <= np.y && np.y < N && vl[np.y][np.x] < np.k) {
						if (ml[np.y][np.x] == '0') {
							vl[np.y][np.x] = np.k;
							q.push(np);
						}
						else if (np.k>1) {
							vl[np.y][np.x] = np.k - 1;
							q.push({ np.x, np.y, np.k - 1 });
						}
					}
				}
			}
		}
		printf("-1");
	}
	return 0;
}