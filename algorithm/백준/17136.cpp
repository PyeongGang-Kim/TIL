#include <stdio.h>
// 0, 0 에서 시작해서 9, 9까지 색종이 채워넣는 경우의 수 다 따져보기.
int vl[10];
int size_list[6] = { 0, 0x1, 0x3, 0x7, 0xf, 0x1f };
int result = 1000;
int all_cnt;
int paper_cnt[6] = { 0, 5, 5, 5, 5, 5 };
bool chk(int x, int y, int size) {
	// size 크기종이 붙일 수 있으면 true 아니면 false 반환.
	// 종이가 있는지 확인부터 해야한다.
	if (!paper_cnt[size]) return false;
	for (int k = y; k < y + size; k++) {
		if ((size_list[size] << x) != (vl[k] & (size_list[size] << x))) {
			return false;
		}
	}
	return true;
}
void solve(int x = 0, int y = 0, int cnt = 0) {
	if (!all_cnt) {
		if (cnt < result) result = cnt;
		return;
	}
	if (y == 10) return;

	// 방문 가능한 곳인지 확인
	if (vl[y] & (1 << x)){
		int rx, ry, rr;
		// 현 위치에서 가장 큰 사각형의 크기 구하기
		rr = 5;
		if (10 - x < rr) rr = 10 - x;
		if (10 - y < rr) rr = 10 - y;
		for (int k = rr; k > 0; k--) {
			if (chk(x, y, k)) {
				// 붙일 수 있는 경우
				for (int l = y; l < y + k; l++) vl[l] -= (size_list[k] << x);
				all_cnt -= k * k;
				paper_cnt[k]--;
				x == 9 ? solve(0, y + 1, cnt + 1) : solve(x + 1, y, cnt + 1);
				all_cnt += k * k;
				paper_cnt[k]++;
				for (int l = y; l < y + k; l++) vl[l] += (size_list[k] << x);
			}
		}
	}
	else {
		x == 9 ? solve(0, y + 1, cnt) : solve(x + 1, y, cnt);
	}
}
int main(void) {
	char tmp;
	int vl_value;
	for (int j = 0; j < 10; j++) {
		vl_value = 0;
		for (int i = 0; i < 10; i++) {
			scanf("%c", &tmp);
			while (tmp < 40) scanf("%c", &tmp);
			if (tmp == '1') {
				all_cnt++;
				vl_value |= 1 << i;
			}
		}
		vl[j] = vl_value;
	}
	solve();
	printf("%d", result == 1000 ? -1 : result);

	return 0;

}