#include <stdio.h>
#include <vector>

using namespace std;

int N, x, lowerIdx, upperIdx;
vector<int> arr;

void lowerBound(int start, int end) {
    int mid = (start + end) / 2;

    if (start > end) return;

    if (arr[mid] == x) {
        lowerIdx = mid;

        lowerBound(start, mid - 1);
    } else if (arr[mid] < x) {
        lowerBound(mid + 1, end);
    } else {
        lowerBound(start, mid - 1);
    }
}

void upperBound(int start, int end) {
    int mid = (start + end) / 2;

    if (start > end) return;

    if (arr[mid] == x) {
        upperIdx = mid + 1;

        upperBound(mid + 1, end);
    } else if (arr[mid] < x) {
        upperBound(mid + 1, end);
    } else {
        upperBound(start, mid - 1);
    }
}

int easyFind() {
    lowerIdx = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
    upperIdx = upper_bound(arr.begin(), arr.end(), x) - arr.begin();

    return upperIdx - lowerIdx;
}

int main() {
    int tmp;

    scanf("%d %d", &N, &x);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &tmp);

        arr.push_back(tmp);
    }

    lowerBound(0, N - 1);
    upperBound(0, N - 1);

    printf("%d %d", upperIdx - lowerIdx, easyFind());

    return 0;
}