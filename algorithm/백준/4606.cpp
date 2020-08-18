#include <stdio.h>
char tmp;
char chk[123];

int main() {
	chk[32] = 1;
	chk[33] = 1;
	chk[36] = 1;
	chk[37] = 1;
	chk[40] = 1;
	chk[41] = 1;
	chk[42] = 1;
	scanf("%c", &tmp);
	while (tmp != '#') {
		while (tmp != '\n') {
			if (chk[tmp]) {
				if (tmp == '*') printf("%%2a");
				else printf("%%%d", tmp - 12);
			}
			else printf("%c", tmp);
			scanf("%c", &tmp);
		}
		printf("\n");
		scanf("%c", &tmp);
	}
	return 0;
}
