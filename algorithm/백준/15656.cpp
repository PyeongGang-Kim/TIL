#include <stdio.h>
int N, M;
int nl[10];
int arr[10];
int result[10];
int num;

void quickSort(int first, int last)
{
	int pivot;
	int i;
	int j;
	int temp;

	if (first < last)
	{
		pivot = first;
		i = first;
		j = last;

		while (i < j)
		{
			while (nl[i] <= nl[pivot] && i < last)
			{
				i++;
			}
			while (nl[j] > nl[pivot])
			{
				j--;
			}
			if (i < j)
			{
				temp = nl[i];
				nl[i] = nl[j];
				nl[j] = temp;
			}
		}

		temp = nl[pivot];
		nl[pivot] = nl[j];
		nl[j] = temp;

		quickSort(first, j - 1);
		quickSort(j + 1, last);
	}
}

int perm(int M, int idx) {
	if (idx == M) {
		for (int i = 0; i < M; ++i) {
			printf("%d ", result[i]);
		}
		printf("\n");
		return 0;
	}
	for (int i = 0; i < N; ++i) {
		result[idx] = nl[i];
		perm(M, idx + 1);
	}

	return 0;
}

int main(void) {

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%d", &nl[i]);

	}
	quickSort(0, N - 1);
	perm(M, 0);

	return 0;

}