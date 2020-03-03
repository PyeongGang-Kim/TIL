#include <stdio.h>
#include <queue>

int T, x1, y1, x2, y2, t1, t2, t3, r;
int abs(int a, int b) {
    return a > b ? a - b : b - a;
}
int main(void) {
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        t1 = abs(x1, x2);
        t2 = abs(y1, y2);
        r = t1 < t2 ? t1*2 : t2*2;
        t3 = abs(t1, t2);
        r += t3 * 2 - (t3 & 1);
        printf("#%d %d\n", tc, r);
    }
    return 0;
}