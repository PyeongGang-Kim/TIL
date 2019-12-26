#include <stdio.h>
#include <vector>
#include <queue>
/*3000000이 최대값 이것보다 크게.

*/
#define maxnumber 20001
#define maxdistance 3000001
using namespace std;
vector<node> nl[20001];
struct node {
	unsigned short ap;
	unsigned char dis;
};
int map[maxnumber];
int V, E, K, u, v, w, s, front, rear, tmp, tmp2, tmp3, cnt;
int main() {
	//pq는 priority_queue<자료구조, 자료구조를 담을 벡터or덱or컨테이너, 비교연산자(less는 최대힙, greater는 최소힙)>
	priority_queue<pair<int, unsigned short>, vector<pair<int, unsigned short> >, greater<pair<int, unsigned short> > > pq;
	scanf("%d %d %d", &V, &E, &s);
	for (int i = 1; i < V + 1; i++) {
		map[i] = maxdistance;
	}
	for (int i = 1; i < E + 1; i++) {
		scanf("%d %d %d", &u, &v, &w);
		node Node = { v, w };
		nl[u].push_back(Node);
	}

	front = 0;
	rear = 1;
	pq.push({ 0, s });
	map[s] = 0;
	while (!pq.empty()) {
		tmp = pq.top().second;
		tmp2 = nl[pq.top().second].size();
		pq.pop();

		for (int j = 0; j < tmp2; j++) {
			tmp3 = map[tmp] + nl[tmp][j].dis;
			if (tmp3 < map[nl[tmp][j].ap]) {
				map[nl[tmp][j].ap] = tmp3;
				pq.push({ tmp3, nl[tmp][j].ap });
			}
		}
	}
	for (int i = 1; i < V + 1; i++) {
		if (map[i] == maxdistance) {
			printf("INF\n");
		}
		else {

			printf("%d\n", map[i]);
		}
	}
	return 0;
}
