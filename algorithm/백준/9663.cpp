#include <stdio.h>
char N;
bool cl1[15];
bool cl2[30];
bool cl3[30];
int res = 0;


//0, 0 / 사선 0번째 1, 0 / 사선 1번째 ... N, N / 사선 2N-1번째까지..
// 반대 사선도 마찬가지로 존재할 것.

//0 0 0 0
//0 0 0 0
//0 0 0 0
//0 0 0 0
// / 사선의 경우i+j번째를 잡으면 된다.
// 반대 사선의 경우 i - j + N-1으로 하면 된다.
void solve(int dep = 0) {
	if (dep == N) {
		res++;
		return;
	}
	for (int i = 0; i < N; i++) {
		if (!cl1[i] && !cl2[i + dep] && !cl3[i - dep + N - 1]) {
			cl1[i] = 1;
			cl2[i + dep] = 1;
			cl3[i - dep + N - 1] = 1;
			solve(dep + 1);
			cl1[i] = 0;
			cl2[i + dep] = 0;
			cl3[i - dep + N - 1] = 0;
		}
	}
}
int main(void) {
	scanf("%hhd", &N);
	solve();
	printf("%d", res);
	return 0;
}