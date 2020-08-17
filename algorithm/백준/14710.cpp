#include <stdio.h>
int h, m;
int main() {
	scanf("%d %d", &h, &m);
	h %= 30;
	if (h * 12 == m)
		printf("O");
	else
		printf("X");
	return 0;
}