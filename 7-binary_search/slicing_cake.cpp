#include <stdio.h>

using namespace std;

int N, M, minVal = 1000000000, maxHeight;
int cakeLen[1000000];

int sliceCake(int height) {
    int sum = 0;
    
    for (int i = 0; i < N; ++i) {
        int slicedLen = cakeLen[i] - height;

        if (slicedLen > 0) {
            sum += slicedLen;
        } 
    }

    return sum;
}

void findHeight(int start, int end) {
    int mid = (start + end) / 2, slicedLen;

    if (start > end) return;

    slicedLen = sliceCake(mid);

    if (slicedLen < M) {
        findHeight(start, mid - 1);
    } else {
        minVal = mid;

        findHeight(mid + 1, end);
    }

}

int main() {
    int tmp;

    scanf("%d %d", &N, &M);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &tmp);
        
        cakeLen[i] = tmp;

        if (tmp > maxHeight) {
            maxHeight = tmp;
        }
    }

    findHeight(0, maxHeight - 1);

    printf("%d", minVal);

    return 0;
}