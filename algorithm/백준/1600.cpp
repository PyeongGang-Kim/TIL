/*
입력 받을때 주의할 점
변수 선언한 형태에 맞춰서 hd hhd 등으로 입력받아야한다.
*/

#include <algorithm>
#include <queue>
short dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 }, dx2[8] = { 1, 2, 2, 1, -1, -2, -2, -1 }, dy2[8] = { -2, -1, 1, 2, 2, 1, -1, -2 };
short W, H;
short K;
bool nl[200][200];
int vl[200][200];
struct pos {
	short x, y, k;
};

int bfs() {
	int time = 0;
	std::queue<pos> q;
	q.push({ 0, 0, K });
	nl[0][0] = 1;
	pos cp, np;
	while (!q.empty()) {
		int qsize = q.size();
		time++;
		while (qsize--) {
			cp = q.front(); q.pop();
			for (int k = 0; k < 4; k++) {
				np = { cp.x + dx[k], cp.y + dy[k], cp.k };
				if (0 <= np.x && np.x < W && 0 <= np.y && np.y < H && !nl[np.y][np.x] && vl[np.y][np.x] < np.k) {
					if (np.x == W - 1 && np.y == H - 1) {
						return time;
					}
					vl[np.y][np.x] = np.k;
					q.push(np);
				}
			}
			if (np.k) {
				for (int k = 0; k < 8; k++) {
					np = { cp.x + dx2[k], cp.y + dy2[k], cp.k - 1 };
					if (0 <= np.x && np.x < W && 0 <= np.y && np.y < H && !nl[np.y][np.x] && vl[np.y][np.x] < np.k) {
						if (np.x == W - 1 && np.y == H - 1) {
							return time;
						}
						vl[np.y][np.x] = np.k;
						q.push(np);
					}
				}
			}
		}
	}
	return -1;
}
int main() {
	scanf("%hd", &K);
	scanf("%hd %hd", &W, &H);
	for (int j = 0; j < H; j++) {
		for (int i = 0; i < W; i++) {
			scanf("%hhd", &nl[j][i]);
		}
	}
	if (W == 1 && H == 1) {
		printf("0");
		return 0;
	}
	for (int j = 0; j < H; j++) for (int i = 0; i < W; i++) vl[j][i] = -1;
	printf("%d", bfs());

	return 0;
}
