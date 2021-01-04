/*
숫자의 최대값을 구했어야하는데 구하지 않은것이 실수
1 51 4 3 2 이런식으로 답이 출력될 수도 있었다.
st, cl 범위 안이어야하고..
입력받은 문자열 길이에 따라서 최대 숫자 값을 계산해야함.
*/


#include <stdio.h>
int N;
int max_num;
char input_value[100];
int st[51];
bool cl[51];
int solve(int dep = 0, int idx = 0) {
	if (dep == N) {
		// 출력 후 종료한다.
		int i = 0;
		while (st[i]) {
			printf("%d ", st[i++]);
		}
		return 1;
	}

	int tmp = input_value[dep] - '0';
	if (!tmp) return 0;

	if (!cl[tmp]) {
		cl[tmp] = 1;
		st[idx] = tmp;
		if (solve(dep + 1, idx + 1)) return 1;
		cl[tmp] = 0;
	}
	tmp = 10 * tmp + input_value[dep + 1] - '0';

	if (tmp > max_num) return 0;
	if (!cl[tmp]) {
		cl[tmp] = 1;
		st[idx] = tmp;
		if (solve(dep + 2, idx + 1)) return 1;
		cl[tmp] = 0;
	}
	return 0;
}

int main(void) {
	scanf("%s", &input_value);
	int i = 0;
	while (input_value[i++]);
	N = i - 1;
	max_num = N < 10 ? N : 9 + ((N - 9) >> 1);
	solve();

	return 0;
}