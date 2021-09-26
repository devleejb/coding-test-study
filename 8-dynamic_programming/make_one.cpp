#include <stdio.h>

using namespace std;

int X, min, tmpResult;
int dp[30001];

int makeOne(int num) {
    printf("%d\n", num);

    if (num == 1) return 0;
    else if (dp[num] != 0) return dp[num];
    else {
        min = 123456789;

        if (num % 3 == 0) {
            tmpResult = makeOne(num / 3);

            min = (min < tmpResult ? min : tmpResult);
        }
        if (num % 5 == 0) {
            tmpResult = makeOne(num / 5);

            min = (min < tmpResult ? min : tmpResult);
        }
        if (num % 2 == 0) {
            tmpResult = makeOne(num / 2);

            min = (min < tmpResult ? min : tmpResult);
        }

        tmpResult = makeOne(num - 1);
        min = (min < tmpResult ? min : tmpResult);
        
        dp[num] = min + 1;

        return min + 1;
    }
}

int main() {
    scanf("%d", &X);

    printf("%d", makeOne(X));

    return 0;
}