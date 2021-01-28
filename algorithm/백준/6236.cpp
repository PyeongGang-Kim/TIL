#include <stdio.h>
#include <algorithm>
// 최소 max_v원 최대 sum_v원
int N, M;
int d[100000];
int sum_v = 0;

bool chk(int v) {
	int m = M;
	int s = 0;
	for (int i = 0; i < N; i++) {
		if (d[i] > s) {
			if (!m) return false;
			m--;
			s = v;
		}
		s -= d[i];
	}
	return true;
}

int ps(int s, int e) {
	if (s == e) {
		return s;
	}
	int m = (s + e) >> 1;
	// m원으로 생활이 가능한 경우 더 작은돈으로 시도
	if (chk(m)) return ps(s, m);
	return ps(m + 1, e);
}


int main(void) {
	int max_v = 0;
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%d", &d[i]);
		sum_v += d[i];
		if (max_v < d[i]) max_v = d[i];
	}
	printf("%d", ps(max_v, sum_v));

	return 0;
}