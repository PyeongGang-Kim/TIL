#include <stdio.h>
#include <algorithm>
int N;
int nl[100000];
int M;
int v;

void bs(int s, int e) {
	if (s == e) {
		printf(nl[s] == v ? "1\n" : "0\n");
		return;
	}
	int m = (s + e) >> 1;
	if (nl[m] > v) {
		bs(s, m);
	}
	else if (nl[m] == v) {
		printf("1\n");
		return;
	}
	else bs(m + 1, e);
}
int main(void) {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) scanf("%d", &nl[i]);
	scanf("%d", &M);
	std::sort(nl, nl + N);
	while (M--) {
		scanf("%d", &v);
		bs(0, N - 1);
	}
	return 0;
}