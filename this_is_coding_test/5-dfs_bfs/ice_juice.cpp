#include <stdio.h>

using namespace std;

int N, M, cnt;
int dx[4] = {0, 1, 0, -1}, dy[4] = {-1, 0, 1, 0}, visited[1000][1000];

void dfs(int row, int col) {
    int nextRow, nextCol;
    
    visited[row][col] = 1;

    for (int i = 0; i < 4; ++i) {
        nextRow = row + dx[i];
        nextCol = col + dy[i];

        if (nextRow >= 0 && nextRow < N && nextCol >= 0 && nextCol < M && visited[nextRow][nextCol] == 0) {
            dfs(nextRow, nextCol);
        }
    }
}

int main() {
    int tmp;

    scanf("%d %d", &N, &M);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%d", &tmp);

            visited[i][j] = tmp;
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (visited[i][j] == 0) {
                ++cnt;
                dfs(i, j);
            }
        }
    }

    printf("%d", cnt);

    return 0;
}