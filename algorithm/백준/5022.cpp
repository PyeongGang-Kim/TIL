#include <stdio.h>
#include <queue>
char a1x, a1y, a2x, a2y, b1x, b1y, b2x, b2y, N, M;
char vl[101][101];
char dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 };
struct pos {
	char x, y;
	std::vector<std::pair<char, char>> st;
};

int bfs(char a1x, char a1y, char a2x, char a2y, char id) {
	std::queue<pos> q;

	//q.front().q.push({ a1x, a1y });
	pos cp, np;
	cp.x = a1x;
	cp.y = a1y;
	cp.st.push_back({ a1x, a1y });
	q.push(cp);
	int dis = 0;
	while (!q.empty()) {
		int qsize = q.size();
		while (qsize--) {
			cp = q.front(); q.pop();
			if (cp.x == a2x && cp.y == a2y) {
				// 종료 조건임. dis를 반환할 것
				id++;
				for (int k = 0; k < cp.st.size(); k++) {
					vl[cp.st[k].second][cp.st[k].first] = id;
				}
				return dis;
			}
			for (int k = 0; k < 4; k++) {
				pos np = { cp.x + dx[k], cp.y + dy[k] };
				if (0 <= np.x && np.x < N && 0 <= np.y && np.y < M && vl[np.y][np.x] < id) {
					vl[np.y][np.x] = id;
					for (int k = 0; k < cp.st.size(); k++) {
						np.st.push_back(cp.st[k]);
					}
					np.st.push_back({ np.x, np.y });
					q.push(np);
				}
			}
		}
		dis++;
	}
	return 0;

}

int abs(char a, char b) {
	if (a < b) return b-a;
	return a-b;
}
int main() {
	// A A 최단거리 후 B B bfs && B B 최단거리 후 A A bfs
	scanf("%hhd %hhd %hhd %hhd %hhd %hhd %hhd %hhd %hhd %hhd", &N, &M, &a1x, &a1y, &a2x, &a2y, &b1x, &b1y, &b2x, &b2y);
	N++; M++;
	int dis, tdis, tmp1, tmp2;
	vl[b1y][b1x] = 1;
	vl[b2y][b2x] = 1;
	tmp1 = bfs(a1x, a1y, a2x, a2y, 1);
	dis = bfs(b1x, b1y, b2x, b2y, 2);
	vl[a1y][a1x] = 4;
	vl[a2y][a2x] = 4;
	tmp2 = bfs(b1x, b1y, b2x, b2y, 4);
	tdis = bfs(a1x, a1y, a2x, a2y, 5);
	if (!dis) {
		if (tdis) {
			dis = tdis + tmp2;
		}
		else dis = 0;
	}
	else {
		if (tdis) {
			if (dis + tmp1 > tdis + tmp2) dis = tdis + tmp2;
			else dis += tmp1;
		}
		else dis += tmp1;
	}
	if (dis) printf("%d", dis);
	else printf("IMPOSSIBLE");
	return 0;
}