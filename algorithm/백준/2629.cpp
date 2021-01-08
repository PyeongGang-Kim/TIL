#include <stdio.h>

// 추 500g에 30개까지 있으므로 최대 무게는 15000이다.
bool vl[2][15001] = { 0, };
short cl[30] = { 0, };
short gl[30] = { 0, };
int main(void) {
	int N;
	int N2;
	scanf("%d", &N);
	for (int i = 0; i < N; i++) scanf("%hd", &cl[i]);
	scanf("%d", &N2);
	for (int i = 0; i < N2; i++) scanf("%hd", &gl[i]);
	vl[0][0] = 1;
	int tmp, tmp2;
	// 짝수번째 추 이용여부 따져 볼때 vl[0]의 값들을 참조해서 vl[1]에
	// 홀수번째는 vl[1]값 참조해서 vl[0]에 기록하면된다.
	// 기록할 때에는 현재 참조하는 값이 있는 경우 +, 0, - 3가지를 추가해주면 된다.
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 15001; j++) {
			if (vl[i & 1][j]) {
				tmp = 1 ^ (i & 1);
				vl[tmp][j] = 1;
				vl[tmp][j - cl[i] < 0 ? cl[i] - j : j - cl[i]] = 1;
				if (j + cl[i] < 15001) vl[tmp][j + cl[i]] = 1;
			}
		}
	}
	tmp = 1 & N;
	for (int i = 0; i < N2; i++) {
		if (gl[i] < 15001) {
			printf("%c ", vl[tmp][gl[i]] ? 'Y' : 'N');
		}
		else printf("N ");
	}

	return 0;
}