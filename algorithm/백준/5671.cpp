#include <stdio.h>

int start, end;

bool itos(int a) {
	int tmp;
	char tmps[5] = { 0, };
	char chk[10] = { 0, };
	chk[a % 10] = 1;

	while (a / 10) {
		a /= 10;
		tmp = a % 10;
		if (!chk[tmp]) {
			chk[tmp] = 1;
		}
		else return 0;
	}
	return 1;
}

int main() {
	char tmp = 0;
	while (scanf("%d %d", &start, &end) == 2) {
		int cnt = 0;
		for (start; start <= end; start++) {
			if (itos(start)) cnt++;
		}
		printf("%d\n", cnt);
	}
	return 0;
}
