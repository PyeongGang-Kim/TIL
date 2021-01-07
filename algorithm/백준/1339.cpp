#include <stdio.h>
/*
이 문제를 푸는 두가지 방법
1. 순열을 이용해서 알파벳에 숫자를 할당하는 방법.

2. 각 자리수를 모두 합산하여 가장 큰 수에 큰 값을 넣는 방법
입력이
AAB
CDE
인 경우
A = 110, B = 1, C = 100, D =  10, E = 1
위와 같이 계산 후 정렬하여 9부터 할당해주면 된다.

*/
char atoi[26];
char arr[11] = { 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
int N;
char word_list[10][9];
char idx = 1;
int result = 0;
void swap(char* a, char* b) {
	char tmp;
	tmp = *a;
	*a = *b;
	*b = tmp;
}
void perm(int dep = 1) {
	if (dep == idx) {
		// 계산후 리턴
		int tmp1;
		int tmp2 = 0;
		for (int j = 0; j < N; j++) {
			tmp1 = 0;
			for (int i = 0; i < 9; i++) {
				if (word_list[j][i]) {
					tmp1 = tmp1 * 10 + arr[atoi[word_list[j][i]]];
				}
				else break;
			}
			tmp2 += tmp1;
		}
		if (tmp2 > result) result = tmp2;
	}
	int tmp;
	for (int tidx = dep; tidx < 11; tidx++) {
		swap(&arr[tidx], &arr[dep]);
		perm(dep + 1);
		swap(&arr[tidx], &arr[dep]);
	}
}

int main(void) {
	scanf("%d", &N);
	for (int k = 0; k < N; k++) {
		scanf("%s", &word_list[k]);
	}
	for (int j = 0; j < N; j++) for (int i = 0; i < 10; i++) {
		if (word_list[j][i]) {
			word_list[j][i] -= 'A' - 1;
			if (!atoi[word_list[j][i]]) atoi[word_list[j][i]] = idx++;
		}
		else break;
	}
	perm();
	printf("%d", result);
	return 0;
}