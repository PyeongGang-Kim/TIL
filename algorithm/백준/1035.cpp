#include <stdio.h>
char D[2][4] = { 0, 1, 0, -1, -1, 0, 1, 0 };
char pts[2][5] = { 0, };
char ptsp = 0;
int pp[571] = { 0, };
int ppp = 0;
int ppng;
char positions[2][5] = { 0, };
int positionp = 0;

int arr[5] = { 0, 1, 2, 3, 4 };
int result = 9999999;
int perm(int i = 0) {
	if (i == ptsp) {
		int tmp = 0;
		for (int k = 0; k < ptsp; k++) {
			tmp += pts[0][arr[k]] > positions[0][k] ? pts[0][arr[k]] - positions[0][k] : positions[0][k] - pts[0][arr[k]];
			tmp += pts[1][arr[k]] > positions[1][k] ? pts[1][arr[k]] - positions[1][k] : positions[1][k] - pts[1][arr[k]];
		}
		if (result > tmp) {
			result = tmp;
		}
		return 0;
	}
	int tmp;
	for (int j = i; j < ptsp; j++) {
		tmp = arr[j];
		arr[j] = arr[i];
		arr[i] = tmp;
		perm(i + 1);
		tmp = arr[j];
		arr[j] = arr[i];
		arr[i] = tmp;
	}
	return 0;
}
int dfs(int i) {
	int cnt = 0;
	ppng -= (1 << i);
	if (ppng < 0) {
		return 0;
	}

	if (i % 5 != 4 && ppng & (1 << (i + 1))) {
		cnt += dfs(i + 1);
	}
	if (i / 5 != 4 && ppng & (1 << (i + 5))) {
		cnt += dfs(i + 5);
	}
	if (i % 5 && ppng & (1 << (i - 1))) {
		cnt += dfs(i - 1);
	}
	if (i / 5 && ppng & (1 << (i - 5))) {
		cnt += dfs(i - 5);
	}
	return cnt + 1;
}
bool chkb(int ppn) {
	int cnt = 0;
	for (int i = 0; i < 25; i++) {
		if (ppn & (1 << i)) {
			ppng = ppn;
			if (dfs(i) == ptsp) {
				return 1;
			}
			return 0;
		}
	}
	if (cnt == ptsp) {
		return 1;
	}
	return 0;
}
void mkp(int dep = 0, int pos = 0, int ppn = 0) {
	if (dep == ptsp) {
		// 해당 숫자의 모든 비트가 붙어있는지 확인한 후 결과값에 넣기
		if (chkb(ppn)) {
			pp[ppp++] = ppn;
		}
		return;
	}
	for (int i = pos; i < 25; i++) {
		mkp(dep + 1, i + 1, ppn + (1 << i));
	}
}

int main() {
	// 조각 갯수와 위치를 센다.
	// 해당 조각 갯수에 맞춰서 경우의 수를 계산한다.
	// 각 경우의 수가 만족하는 것들만 남긴다.
	// 최고 많은 경우의 수는 25C5 = 53130이다.
	// 처음 조각 위치에서 각 경우의 수 별로 최소 횟수를 구한다(최대 5!)
	// 최소값을 갱신한다.
	// pts에 각 별의 위치를 기록 ptsp가 별의 갯수
	char tmp[6];
	int j = 0;
	while (j < 5) {
		scanf("%s", &tmp);
		for (int i = 0; i < 5; i++) {
			if (tmp[i] == '*') {
				pts[0][ptsp] = i;
				pts[1][ptsp++] = j;
			}
		}
		j++;
	}
	// 별의 갯수에 맞춰 경우의 수 생성
	mkp();

	int cp;
	for (int i = 0; i < ppp; i++) {
		positionp = 0;
		while (pp[i]) {
			for (int k = 0; k < 25; k++) {
				if ((1<<k) == pp[i] - (pp[i] & (pp[i] - 1))) {
					positions[0][positionp] = k % 5;
					positions[1][positionp++] = k / 5;
					break;
				}
			}
			pp[i] &= pp[i] - 1;
		}
		perm();
	}
	printf("%d", result);
	return 0;
}
