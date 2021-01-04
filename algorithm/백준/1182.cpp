#include <stdio.h>
int N;
int arr[21];
int res;
int S;
void solve(int dep = 0, int tmp_s = 0, bool chk = false) {
	if (dep == N){
		if (chk && tmp_s == S) res++;
		return;
	}
	solve(dep + 1, tmp_s + arr[dep], true);
	solve(dep + 1, tmp_s, chk);
	return;
}
int main(void) {
	scanf("%d %d", &N, &S);
	for (int i = 0; i < N; i++) scanf("%d", &arr[i]);
	solve();
	printf("%d", res);
	return 0;
}