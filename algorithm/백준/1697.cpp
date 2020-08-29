#include <stdio.h>
#include <queue>

bool vl[200001] = { 0, };
int main() {
	// 방문했던 곳 방문처리
	// 일정 범위 벗어난 경우 예외처리
	std::queue<std::pair<int, int>>q;
	int N, K;
	scanf("%d %d", &N, &K);
	q.push({ N, 0 });
	std::pair<int, int> cp, np;
	while (!q.empty()) {
		cp = q.front();
		if (cp.first == K) {
			printf("%d", cp.second);
			break;
		}
		// K보다 크면 +1, 2배일 필요 없다
		// 0보다 작으면 -1 할 필요 없다.
		//        0            K
		// *2 +1    *2  +1 -1     -1
		if (cp.first < K) {
			// +1, *2
			if (!vl[cp.first + 1]) {
				q.push({ cp.first + 1, cp.second + 1 });
				vl[cp.first + 1] = 1;
			}
			if (!vl[cp.first << 1]) {
				q.push({ cp.first << 1, cp.second + 1 });
				vl[cp.first << 1] = 1;
			}
		}
		if (cp.first > 0) {
			// -1
			if (!vl[cp.first - 1]) {
				q.push({ cp.first - 1, cp.second + 1 });
				vl[cp.first - 1] = 1;
			}
		}
		q.pop();
	}
	return 0;
}
