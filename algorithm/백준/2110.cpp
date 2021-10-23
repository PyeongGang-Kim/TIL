#include <stdio.h>
#include <algorithm>
int N, C;
int d[200000];

bool chk(int v) {
    // 0번 인덱스에 공유기 설치 후
    // 이전 설치 위치에서 거리 v이상인 곳에서 공유기 설치
    // 정렬된 배열임으로 어떤 경우에 대해서도 성립.
	int c = C-1;
	int j = 0;
	for (int i = 1; i < N; i++) {
		if (d[i] - d[j] >= v) {
			j = i;
			c--;
			if (!c) return true;
		}
	}
	return false;
}


int ps(int s, int e) {
	if (s == e) {
		if (chk(s)) return s;
		return s-1;
	}
	int m = (s + e) >> 1;

	// 거리 m일때 가능한지 확인하기
	if (chk(m)) return ps(m + 1, e);
	return ps(s, m);
}


int main(void) {
	scanf("%d %d", &N, &C);
	for (int i = 0; i < N; i++) scanf("%d", &d[i]);
	std::sort(d, d + N);

	printf("%d", ps(0, 1000000000));
}