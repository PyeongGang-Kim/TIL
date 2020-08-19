#include <stdio.h>
int N;
char pl[20][201] = { 0, };
int K;
char tmp[201] = { 0, };
int main() {
	scanf("%d", &N);
	int i = 0;
	scanf("%s[^\n]", tmp);
	while (tmp[i++]);
	K = i / N;
	int dy = 1;
	int x = 0;
	int y = 0;
	i = 0;
	while (1) {
		pl[y][x] = tmp[i++];
		if (!tmp[i]) break;
		y += dy;
		if (y < 0 || y >= N) {
			dy = dy == 1 ? -1 : 1;
			y += dy;
			x++;
		}
	}
    for (int j = 0; j < N; j++){
        for (int i = 0; i < K; i++){
            printf("%c", pl[j][i]);
        }
    }
	printf("\n");
	return 0;
}
