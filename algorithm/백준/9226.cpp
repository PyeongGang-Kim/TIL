#include <stdio.h>
char a[31];
short chk[123];
int main() {
	chk['a'] = 1;
	chk['e'] = 1;
	chk['i'] = 1;
	chk['o'] = 1;
	chk['u'] = 1;
	while (1) {
		scanf("%s", &a);
		if (a[0] == '#') return 0;
		int i = 0;
		while (a[i]) {
			if (chk[a[i]]) {
				break;
			}
			i++;
		}
		if (a[i]) {
			for (int j = i; a[j]; j++) {
				printf("%c", a[j]);
			}
			for (int j = 0; j < i; j++) {
				printf("%c", a[j]);
			}
			printf("ay\n");
		}
		else {
			for (i = 0; a[i]; i++) {
				printf("%c", a[i]);
			}
			printf("ay\n");
		}
	}
	return 0;
}
