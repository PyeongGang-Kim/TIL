#include <stdio.h>
#include <algorithm>
// 주의 할 점. 어떤 경우에도 구간의 크기가 줄어들 수 있도록 m 값을 구성해야 함.
// m = (s+e) >> 1 인 경우 양 구간은 (s, m), (m+1, e) 이어야 한다. 종료 조건에서 해당 구간에서 가능한지 확인해 볼 필요가 있다.
int N, M;
int sum_array[10000];
int d[10000];
int sum_v;

int bs(int s, int e, int v) {
	// v 값보다 작거나 같은 최대 인덱스 찾기
	if (s + 1 >= e) {
		if (d[e] <= v) return e;
		if (d[s] > v) return s - 1;
		return s;
	}
	int m = (s + e) >> 1;
	if (d[m] > v) return bs(s, m, v);
	else if (d[m] < v) return bs(m+1, e, v);
	else return m;
}


int ps(int s, int e) {
	// 탈출 조건일 때 s에서 불가능 한 경우 s-1 리턴하기
	if (s == e) {
		int cur = bs(0, N - 1, s);
		int tmp = (N - cur - 1) * s;
		if (cur != -1) tmp += sum_array[cur];
		if (tmp > M) return s - 1;
		return s;
	}
	int m = (s + e) >> 1;
	// 가장 높은 높이를 찾아야 한다.
	// 현재 높이가 m이라고 할 때의 총 예산?
	int tmp;
	int cur = bs(0, N - 1, m);
	tmp = (N - cur - 1) * m;
	if (cur != -1) tmp += sum_array[cur];

	if (tmp < M) return ps(m+1, e);
	else if (tmp > M) return ps(s, m);
	else return m;
}

int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) scanf("%d", &d[i]);
	std::sort(d, d + N);
	scanf("%d", &M);
	sum_array[0] = d[0];
	int max_v = d[0];
	for (int i = 1; i < N; i++) {
		sum_array[i] = sum_array[i - 1] + d[i];
		if (max_v < d[i]) max_v = d[i];
	}
	sum_v = sum_array[N - 1];
	printf("%d", ps(0, max_v));
	return 0;
}