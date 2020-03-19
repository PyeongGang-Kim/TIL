#include <stdio.h>

int N;
int st[1000000];
int num;
int tmp;
int stidx;

void bs(int num, int s, int e) {
	if (s == e || s + 1 == e) {
		if (st[s] < num) {
			st[s + 1] = num;
		}
		else {
			st[s] = num;
		}
		return;
	}
	int	m = (s + e) >> 1;
	if (num < st[m]) {
		bs(num, s, m);
	}
	else if (st[m] < num) {
		bs(num, m + 1, e);
	}

}
int main() {
	scanf("%d", &N);
	stidx = 0;
	for (N; N; N--) {
		scanf("%d", &num);
		if (num > st[stidx]) {
			st[++stidx] = num;
		}
		else if (st[stidx] > num) {
			bs(num, 0, stidx);
		}
	}
	printf("%d\n", stidx);
}