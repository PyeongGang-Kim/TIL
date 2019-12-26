#include <stdio.h>
#include <queue>
int nl[1001][1001];
int dist[1001];
int N, M, s, e, d, S, G, tmp;
using namespace std;
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;

int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		dist[i] = 1000000000;
		for (int j = 1; j <= N; j++) {
			nl[j][i] = 1000000;
		}
	}

	scanf("%d", &M);
	while (M--) {
		scanf("%d %d %d", &s, &e, &d);
		if (nl[s][e]<=100000) {
			if (nl[s][e] > d) {
				nl[s][e] = d;
			}
		}
		else {
			nl[s][e] = d;
		}
	}
	scanf("%d %d", &S, &G);
	pq.push({ 0, S });
	dist[S] = 0;
	while (!pq.empty()) {
		tmp = pq.top().second;
		pq.pop();
		for (int i = 1; i <= N; i++) {
			if (nl[tmp][i]<=100000) {
				if (nl[tmp][i] + dist[tmp] < dist[i]) {
					dist[i] = nl[tmp][i] + dist[tmp];
					pq.push({ dist[i], i });
				}
			}
		}
	}
	printf("%d\n", dist[G]);
}