#include <stdio.h>
#include <vector>

int arr1[10];
int arr2[10];
int K;
char tmp;
int idx;
int tmpl1[10];
int tmpl2[10];
int r1[10];
int r2[10];
int val;

void result(int arr[], int val, int tmpl[]) {
	for (int i = 0; i <= K; i++) {
		if (!arr[i]) {
			for (int j = i; j <= K; j++) {
				if (tmpl[j] || j == K) {
					for (int l = j; l >= i; l--) {
						arr[l] = val--;
					}
					break;
				}
			}
		}
	}

}
int main(void) {
	scanf("%d", &K);
	idx = K-1;
	for (int k = 0; k < K; k++) {
		scanf("%c", &tmp);
		while (!(tmp == '<' || tmp == '>')) {
			scanf("%c", &tmp);
		}
		tmpl1[k] = tmp == '<' ? 0 : 1;
		tmpl2[idx--] = !tmpl1[k];
	}
	result(r1, 9, tmpl1);
	result(r2, K, tmpl2);
	for (int i = 0; i <= K; i++) {
		printf("%d", r1[i]);
	}
	printf("\n");
	for (int i = K; i >= 0; i--) {
		printf("%d", r2[i]);
	}
	return 0;
}