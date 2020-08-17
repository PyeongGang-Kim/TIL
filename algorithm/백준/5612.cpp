#include <stdio.h>
int n, m;
int a, b;
int max;
int main() {
	scanf("%d", &n);
	scanf("%d", &m);
	max = m;

	while (n--) {
		scanf("%d %d", &a, &b);
		m += a - b;
		if (m < 0) {
			break;
		}
		if (max < m)
			max = m;
	}
	if (m < 0) {
		printf("0");
	}
	else {
		printf("%d", max);
	}
	return 0;
}