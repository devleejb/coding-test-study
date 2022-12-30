#include <stdio.h>

using namespace std;

int N;
int stock[101], dp[101];

void stealStock() {
    int steal, notSteal;

    dp[1] = stock[1];

    for (int i = 2; i <= N; ++i) {
        steal = dp[i - 2] + stock[i];
        notSteal = dp[i - 1];

        dp[i] = steal > notSteal ? steal : notSteal;
    }
}

int main() {
    scanf("%d", &N);

    for (int i = 1; i <= N; ++i) {
        scanf("%d", &stock[i]);
    }

    stealStock();

    printf("%d", dp[N]);

    return 0;
}