#include <stdio.h>

int nl[21] = { 0, };
int min(int A, int B) {
	if (A > B) return B;
	return A;
}
bool solve(int L, int W, int H) {
	if (!(L && W && H)) return true;
	int cs = min(H, min(L, W));
	int idx;
	while (cs) {
		idx = cs & (cs - 1);
		if (!idx) break;
		cs = idx;
	}
	idx = 0;
	while (idx < 21) {
		if (cs & (1 << idx++)) break;
	}
	idx--;

	long long num = 1;
	while (num) {
		if (nl[idx]) {
			if (nl[idx] < num) {
				num -= nl[idx];
				nl[idx] = 0;
			}
			else {
				nl[idx] -= num;
				num = 0;
			}
		}
		if (!idx) break;
		num <<= 3;
		idx -= 1;
	}
	if (num) return false;
	if (!solve(L, W, H - cs)) return false;
	if (!solve(L - cs, W, cs)) return false;
	if (!solve(cs, W - cs, cs)) return false;
	return true;

}

int abs(char a, char b) {
	if (a < b) return b-a;
	return a-b;
}
int main() {
	int L, W, H;
	scanf("%d %d %d", &L, &W, &H);
	int n;
	scanf("%d", &n);
	int a, b;
	while (n--) {
		scanf("%d %d", &a, &b);
		nl[a] = b;
	}
	int r = 0;
	for (int i = 0; i < 21; i++) r += nl[i];

	if (solve(L, W, H)) {
		int r2 = 0;
		for (int i = 0; i < 21; i++) r2 += nl[i];
		printf("%d", r - r2);
	}
	else printf("-1");

	return 0;
}