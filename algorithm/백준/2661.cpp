#include <stdio.h>
/*
맨 마지막에 숫자 하나 추가될 때마다 해당 길이에서 볼 수 있는 값들을 비교해보면서 해야한다.
*/
int N;
char number[81];

bool solve(int dep = 0) {
	if (dep == N) {
		// 출력 후 리턴;
		for (int i = 0; i < N; i++) printf("%d", number[i]);
		printf("\n");
		return true;
	}
	// 1, 2, 3을 붙여 보면서 가능한지 볼 것.
	for (int k = 1; k < 4; k++) {
		number[dep] = k;
		int tmp = (dep + 1) >> 1;
		// 동일한 조합이 있는지 확인하기. 하나라도 있으면 안된다.
		bool chk = false;
		for (int i = 1; i < tmp + 1; i++) {
			for (int j = dep; j > dep - i; j--) {
				if (number[j] != number[j - i]) break;
				if (j == dep - i + 1) chk = true;
			}
			if (chk) break;
		}
		if (!chk && solve(dep + 1)) {
			return true;
		}
	}
	return false;
}
int main(void) {
	scanf("%d", &N);
	solve();
	return 0;
}