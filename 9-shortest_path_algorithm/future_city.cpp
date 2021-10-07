#include <stdio.h>
#include <algorithm>

#define INF 123456789

using namespace std;

int N, M, X, K;
int d[101][101];

void floydWarshall() {
    for (int v = 1; v <= N; ++v) {
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (d[v][i] > d[v][j] + d[j][i]) {
                    d[v][i] = d[v][j] + d[j][i];
                }
            }
        }
    }
}

int main() {
    int from, to;

    scanf("%d %d", &N, &M);

    for (int i = 1; i <= N; ++i) {
        fill(d[i], d[i] + N + 1, INF);
        d[i][i] = 0;
    }

    for (int i = 0; i < M; ++i) {
        scanf("%d %d", &from, &to);
        d[from][to] = d[to][from] = 1;
    }

    scanf("%d %d", &X, &K);

    floydWarshall();

    if (d[1][K] == INF || d[K][X] == INF) {
        printf("-1");
    } else {
        printf("%d", d[1][K] + d[K][X]);
    }

    return 0;
}