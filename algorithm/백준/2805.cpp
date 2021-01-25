#include <stdio.h>
#include <algorithm>
// int와 long long 연산을 하면 중간에 int로 변환되는 문제가 있으니 유의할 것.
// long long의 경우 출력시에도 lld로 출력해야 함을 유의할 것.


typedef long long ll;
int N, M;
long long trees[1000000];
long long sum_array[1000000];
int bs(int s, int e, ll num) {
	if (s >= e) return e;
	// 배열과 찾는 값을 입력받으면 해당 값이 존재하는 인덱스를 반환한다.
	int m = (s + e) >> 1;

	if (trees[m] > num) return bs(s, m, num);
	else if (trees[m] == num) return m;
	else return bs(m + 1, e, num);
}
long long ps(ll s, ll e) {
	if (s + 1 >= e) {
		// e에서 가능하면 e일때의 값
		// 불가능하면 s일때의 값
		int cur = bs(0, N - 1, e);
		// (N -  현재 인덱스) * 현재 높이
		ll tmp = sum_array[N - 1] - sum_array[cur - 1] - (N - cur) * e;//잘린 나무 길이 합

		if (tmp >= M) return e;
		else return s;
	}
	ll m = (s + e) >> 1;

	ll cur = bs(0, N - 1, m);
	// (N -  현재 인덱스) * 현재 높이
	ll tmp;
	if (!cur) {
		tmp = sum_array[N - 1] - (N - cur) * m;//잘린 나무 길이 합
	}
	else {
		tmp = sum_array[N - 1] - sum_array[cur - 1] - (N - cur) * m;//잘린 나무 길이 합
	}
	// M보다 tmp가 작으면 무조건 높이를 줄여야한다.
	// 같으면? 현재 높이를 반환하면 된다.
	// 크면? 높이를 높인다..
	if (tmp < M) return ps(s, m-1);
	else if (tmp == M) return m;
	else return ps(m, e);


}
int main(void) {
	// 합배열, 인덱스
	// 파라메트릭 서치
	scanf("%d %d", &N, &M);
	int i = N;
	while (i--) {
		scanf("%lld", &trees[i]);
	}
	std::sort(trees, trees + N);

	ll treesum = trees[0];


	sum_array[0] = trees[0];
	ll max_v = 0;
	if (max_v < trees[0]) max_v = trees[0];
	for (int i = 1; i < N; i++) {
		if (max_v < trees[i]) max_v = trees[i];
		treesum += trees[i];
		sum_array[i] += sum_array[i-1] + trees[i];
	}
	printf("%lld", ps(0, max_v));


	return 0;
}