#include <stdio.h>
// s. e가 중간에 더해질 때 int 범위를 초과하는 경우 문제가 발생한다.
// (int + int) >> 1 이 최종적으로 int 범위라고 하더라도 문제가 생길 수 있음.
// (s + (long long)e) >>1로 변환하면 연산의 결과가 longlong형으로 계산되서 오버플로우 문제 해결됨.

int N, K;
int d[10000];

bool chk(unsigned int v) {
	if (!v) return true;
	int w = N;
	int tmp;
	for (int i = 0; i < K; i++) {
		tmp = d[i] / v;
		w -= tmp;
		if (w <= 0) return true;
	}
	return false;
}


int ps(unsigned int s, unsigned int e) {
	if (s == e) {
		if (chk(s)) return s;
		return s-1;
	}
	int m = (s + e) >> 1;

	// 길이 m으로 N개의 전선 만들수 있다면 더 길게 해보기
	if (chk(m)) return ps(m + 1, e);
	return ps(s, m);
}


int main(void) {
	scanf("%d %d", &K, &N);
	unsigned int max_v = 0;
	for (int i = 0; i < K; i++) {
		scanf("%d", &d[i]);
		if (max_v < d[i]) max_v = d[i];
	}
	printf("%d", ps(0, max_v));
}