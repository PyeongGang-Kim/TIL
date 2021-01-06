#include <stdio.h>
#include <algorithm>
int L, C;
char result[20];
char input_value[20];

bool chk_s(char spel) {
	if (spel == 'a' || spel == 'e' || spel == 'i' || spel == 'o' || spel == 'u') return true;
	return false;
}
void comb(int cnt=0, int dep=0, int cnt_m=0, int cnt_j=0) {
	if (cnt == L) {
		// 출력 후 리턴
		if (cnt_m && cnt_j > 1) {
			for (int i = 0; i < L; i++) printf("%c", result[i]);
			printf("\n");
		}
		return;
	}
	if (dep == C) return;
	for (int i = dep; i < C; i++) {
		if (cnt) {
			// 이전 글자와 비교하기
			if (result[cnt - 1] < input_value[i]) {
				result[cnt] = input_value[i];
				chk_s(result[cnt]) ? comb(cnt + 1, i + 1, cnt_m + 1, cnt_j) : comb(cnt + 1, i + 1, cnt_m, cnt_j + 1);
			}
		}
		else {
			// 그냥 바로 글자 넣고 다음글자 확인하기
			result[cnt] = input_value[i];
			chk_s(result[cnt]) ? comb(cnt + 1, i + 1, cnt_m + 1, cnt_j) : comb(cnt + 1, i + 1, cnt_m, cnt_j + 1);
		}
	}
}

int main(void) {
	scanf("%d %d", &L, &C);
	int i = 0;
	for (int i = 0; i < C; i++) {
		scanf("%c", &input_value[i]);
		if (input_value[i] < 40) i--;
	}
	std::sort(input_value, input_value + C);

	comb();
}