#include <stdio.h>
#include <queue>

int N;
char tmp;
int tmpidx;
char al[101][11];
int inf = 0xFFFFFFF;
int ml[123][123];
int cnt[126] = { 0 };
int vl[123] = { 0 };
int vlcnt = 0;
char result[30];
int chk = 0;
void mke(int idx, int s, int e) {
	char tmp;
	char tmpidx;
	tmp = al[s][idx];
	tmpidx = s;
	for (int i = s+1; i < e; i++) {
		if (al[i][idx] != tmp) {
			if (tmp != '\0') {
				mke(idx + 1, tmpidx, i);
				if (!ml[tmp][al[i][idx]]) {

					if (!al[i][idx]) {
						chk = 1;
					}
					ml[tmp][al[i][idx]] = 1;
					cnt[al[i][idx]] += 1;
				}
			}
			tmp = al[i][idx];
			tmpidx = i;
		}
		if (tmp != '\0' && i == e - 1 && tmpidx != i) {
			mke(idx + 1, tmpidx, i + 1);
		}
	}


}

int main(void) {
	scanf("%d", &N);
	int N2 = N;
	for (int i = 0; i < N; i++) {
		scanf("%s", &al[i]);
	}
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < 11; i++) {
			if (al[j][i] == '\0') {
				break;
			}
			if (!vl[al[j][i]]) {
				vl[al[j][i]] = 1;
				vlcnt += 1;
			}
		}
	}
	mke(0, 0, N);
	/*for (int i = 97; i < 123; i++) {
		printf("%c", i);
	}
	printf("\n");
	for (int j = 97; j < 123; j++) {
		for (int i = 97; i < 123; i++) {
			printf("%d", ml[j][i]==inf?0:ml[j][i]);
		}
		printf("%c\n", j);
	}*/
	std::queue<int> Q;
	int ridx = 0;
	for (int i = 97; i < 123; i++) {
		// 들어오는 놈이 0개인 것들만 모두 넣는다. 필요한거? 다음위치로 갈 인덱스
		if (!cnt[i] && vl[i]) {
			Q.push(i);
		}
	}
	int idx = 0;
	int chk2 = 0;
	int chkl[100] = { 0 };

	while (!Q.empty()) {
		if (Q.size() > 1) {
			chk2 = 1;
		}
		idx = Q.front();
		vlcnt--;
		result[ridx++] = idx;
		Q.pop();
		for (int j = 97; j < 123; j++) {
			if (ml[idx][j]) {
				cnt[j] -= 1;
				if (!cnt[j]) {
					Q.push(j);
				}
			}
		}
	}
	if (vlcnt) {
		chk = 1;
	}
	if (chk) {
		printf("!");
	}
	else {
		if (chk2) {
			printf("?");
		}
		else {
			printf("%s", result);
		}
	}

	return 0;
}