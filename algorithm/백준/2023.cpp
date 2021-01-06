#include <stdio.h>
int N;

bool is_Prime(int num) {
	for (int i = 2; i < num >> 1; i++) {
		if (!(num % i)) return false;
	}
	return true;
}


void mkp(int cur_num, int dep = 1) {
	if (dep == N) {
		// 출력 후 리턴하기
		printf("%d\n", cur_num);
		return;
	}
	cur_num *= 10;
	for (int i = 0; i < 10; i++) {
		if (is_Prime(cur_num + i)) {
			mkp(cur_num + i, dep + 1);
		}
	}
	return;
}


int main(void) {
	scanf("%d", &N);
	mkp(2);
	mkp(3);
	mkp(5);
	mkp(7);
}