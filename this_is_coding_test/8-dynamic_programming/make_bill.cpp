#include <stdio.h>

using namespace std;

int N, M, tmp;
int price[100], dp[10001];

void makeBill() {
    for (int i = 1; i <= M; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i - price[j] > 0 && dp[i - price[j]] != 0) {
                tmp = dp[i - price[j]] + 1;

                if (dp[i] == 0 || dp[i] > tmp) {
                    dp[i] = tmp;
                }
            }
        }
    }
}

int main() {
    scanf("%d %d", &N, &M);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &tmp);

        price[i] = tmp;
        dp[tmp] = 1;
    }
    
    makeBill();

    tmp = dp[M] == 0 ? -1 : dp[M];

    printf("%d", tmp);

    return 0;
}