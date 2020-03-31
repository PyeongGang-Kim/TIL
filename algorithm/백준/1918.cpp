#include <stdio.h>
char O[101];
char st[105];
int rear;
int len_O;
int main(void) {
	scanf(" %s", &O);
	rear = -1;
	len_O = 0;
	for (int i = 0; O[i]; i++) {
		len_O++;
	}
	for (int i = 0; i < len_O; i++) {
		if (O[i] == '(')
			st[++rear] = '(';
		else if (O[i] == ')') {
			while (st[rear] != '(')
				printf("%c", st[rear--]);
			rear--;
		}
		else if (O[i] == '+' || O[i] == '-') {
			while (rear > -1 && st[rear] != '(')
				printf("%c", st[rear--]);
			st[++rear] = O[i];
		}
		else if (O[i] == '*' || O[i] == '/') {
			while (rear > -1 && st[rear] != '(' && st[rear] != '+' && st[rear] != '-')
				printf("%c", st[rear--]);
			st[++rear] = O[i];
		}
		else
			printf("%c", O[i]);
	}
	while (rear > -1)
		printf("%c", st[rear--]);
	return 0;
}

