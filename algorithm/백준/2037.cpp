#include <stdio.h>
char st[1001];
int d[100][2];
int i, p, w, tmp, result;
int main() {
	for (i = 65; i < 83; i++) {
		d[i][0] = (i-59) / 3;
		d[i][1] = (i-59) % 3 + 1;
	}
	d[83][0] = 7;d[83][1] = 4;
	for (i = 84; i < 90; i++) {
		d[i][0] = (i - 60) / 3;
		d[i][1] = (i - 60) % 3 + 1;
	}
	d[90][0] = 9;d[90][1] = 4;d[32][1] = 1;
	scanf("%d %d", &p, &w);
	i = 0;
	while (st[0] != '\n') scanf("%c", &st[0]);
	scanf("%c", &st[0]);
	while (st[i++]!='\n') scanf("%c", &st[i]);
	i = 0;
	tmp = 0;
	result = 0;
	while (st[i] != '\n') {
		if ((d[st[i]][0] == tmp) && (tmp !=d[' '][0])) {
			result += w;
		}
		else tmp = d[st[i]][0];
		result += p * d[st[i]][1];
		i++;
	}
	printf("%d", result);
	return 0;
}
