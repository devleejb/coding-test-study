#include <stdio.h>

using namespace std;

int N, maxVal;
int soldier[2000], dp[2000];

void putSoldier() {
    for (int i = 0; i < N; ++i) {
        dp[i] = 1;

        for (int j = 0; j < i; ++j) {
            if (soldier[j] > soldier[i]) {
                dp[i] = dp[i] > dp[j] + 1 ? dp[i] : (dp[j] + 1);

                if (dp[i] > maxVal) maxVal = dp[i];
            }
        }
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &soldier[i]);
    }

    putSoldier();

    printf("%d", maxVal);

    return 0;
}