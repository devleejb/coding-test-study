#include <stdio.h>

using namespace std;

int T, n[1000], m[1000], gold[1000][20][20], dp[1000][20][20], result[1000];
int dr[3] = {-1, 0, 1};

void getGold() {
    for (int i = 0; i < T; ++i) {
        for (int c = 0; c < m[i]; ++c) {
            for (int r = 0; r < n[i]; ++r) {
                if (c == 0) {
                    dp[i][r][c] = gold[i][r][c];
                } else {
                    for (int d = 0; d < 3; ++d) {
                        if (r + dr[d] >= 0 && r + dr[d] < n[i]) {
                            dp[i][r][c] = dp[i][r][c] > dp[i][r + dr[d]][c - 1] + gold[i][r][c] ? dp[i][r][c] : dp[i][r + dr[d]][c - 1] + gold[i][r][c];
                        }
                    }
                }
            }
        }

        for (int r = 0; r < n[i]; ++r) {
            result[i] = result[i] > dp[i][r][m[i] - 1] ? result[i] : dp[i][r][m[i] - 1];
        }
    }
}

int main() {
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        scanf("%d %d", &n[i], &m[i]);

        for (int r = 0; r < n[i]; ++r) {
            for (int c = 0; c < m[i]; ++c) {
                scanf("%d", &gold[i][r][c]);
            }
        }
    }

    getGold();

    for (int i = 0; i < T; ++i) {
        printf("%d\n", result[i]);
    }

    return 0;
}