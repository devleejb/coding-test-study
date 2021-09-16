#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int N, K, sum;
vector<int> A, B;

int main() {
    int tmp;

    scanf("%d %d", &N, &K);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &tmp);

        A.push_back(tmp);
    }

    for (int i = 0; i < N; ++i) {
        scanf("%d", &tmp);

        B.push_back(tmp);
    }

    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    for (int i = 0; i < K; ++i) {
        if (B[N - 1 - i] > A[i]) {
            swap(B[N - 1 - i], A[i]);
        } else {
            break;
        }
    }

    for (int i = 0; i < N; i++) {
        sum += A[i];
    }
    
    printf("%d", sum);

    return 0;
}
