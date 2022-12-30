#include <stdio.h>
#include <queue>

using namespace std;

int N, M;
int dx[4] = {0, 1, 0, -1}, dy[4] = {-1, 0, 1, 0}, maze[200][200], dis[200][200];

void bfs() {
    queue<int> rq, cq;
    int nowRow, nowCol, nextRow, nextCol;

    rq.push(0);
    cq.push(0);
    dis[0][0] = 1;

    while (!rq.empty()) {
        nowRow = rq.front();
        nowCol = cq.front();

        rq.pop();
        cq.pop();

        for (int i = 0; i < 4; ++i) {
            nextRow = nowRow + dy[i];
            nextCol = nowCol + dx[i];

            if (nextRow >= 0 && nextRow < N && nextCol >= 0 && nextCol < M && maze[nextRow][nextCol] == 1 && dis[nextRow][nextCol] == 0) {
                dis[nextRow][nextCol] = dis[nowRow][nowCol] + 1;

                rq.push(nextRow);
                cq.push(nextCol);
            }
        }
    }
}

int main() {
    scanf("%d %d", &N, &M);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%1d", &maze[i][j]);
        }
    }

    bfs();

    printf("%d", dis[N - 1][M - 1]);

    return 0;
}