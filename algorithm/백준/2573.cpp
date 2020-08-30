#include <stdio.h>
#include <queue>
#include <vector>
char nl[300][300];
int vl[300][300];
int N, M;
short limit[4] = { 0, };
int time = 1;
struct meltpoint {
	short x, y;
	char k;
};
int iceCount;

// 벡터 활용해서 녹을곳만 벡터에 삽입하기
int fs() {
	int dx[4] = { 0, 1, 0, -1 }, dy[4] = { -1, 0, 1, 0 };

	std::pair<short, short> cp, np;
	while (1) {
		short tx, ty;
		for (short j = limit[1]; j < N; j++) {
			int ccc = 0;
			for (short i = 0; i < M; i++) if (nl[j][i]) {
				std::vector<meltpoint> mp;
				int iceCount2 = 1;
				ccc = 1;
				limit[1] = j;
				// 시작 좌표 찾았으니 여기서부터 bfs
				std::queue<std::pair<short, short>> q;
				q.push({ i, j });
				vl[j][i] = time;
				while (!q.empty()) {
					cp = q.front(); q.pop();
					char cnt = 0;
					for (int k = 0; k < 4; k++) {
						tx = cp.first + dx[k];
						ty = cp.second + dy[k];
						if (!nl[ty][tx]) {
							cnt++;
						}
						else if (vl[ty][tx] < time) {
							vl[ty][tx] = time;
							q.push({ tx, ty });
							iceCount2++;
						}
					}
					// 얼마만큼 녹을지 기록
					if (cnt) mp.push_back({ cp.first, cp.second, cnt });
				}
				if (iceCount2 != iceCount) return time;
				// 녹은것이 없으면 반복해서 녹이기
				bool chk = 0;
				while (!chk) {
					for (int k = 0; k < mp.size(); k++) {
						if (nl[mp[k].y][mp[k].x]) {
							if (nl[mp[k].y][mp[k].x] > mp[k].k) {
								nl[mp[k].y][mp[k].x] -= mp[k].k;
							}
							else {
								nl[mp[k].y][mp[k].x] = 0;
								// 전체얼음갯수 감소시키기
								chk = 1;
								iceCount--;
							}
						}
					}
					time++;
				}

				if (!iceCount) return 1;
			}
			if (ccc) break;
		}
	}
	return 1;
}
int main() {
	// 얼음 녹인다. 빙산 중 한 곳에서 bfs 한다.
	// 쪼개졌으면 시간 반환
	// 녹일게 없으면 0 반환
	scanf("%d %d", &N, &M);
	for (int j = 0; j < N; j++) for (int i = 0; i < M; i++) scanf("%hhd", &nl[j][i]);
	iceCount = 0;
	for (int j = 0; j < N; j++) for (int i = 0; i < M; i++) if (nl[j][i]) iceCount++;
	printf("%d", fs()-1);

	return 0;
}