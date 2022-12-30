#include <stdio.h>

using namespace std;

int row, col, cnt;
int dx[8] = {-2, -2, -1, 1, 2, 2, 1, -1}, dy[8] = {-1, 1, 2, 2, 1, -1, -2, -2};

void countCase() {
    int destRow, destCol;

    for (int i = 0; i < 8; ++i) {
        destRow = row + dx[i];
        destCol = col + dy[i];

        if (destRow > 0 && destRow <= 8 && destCol > 0 && destCol <= 8) {
            ++cnt;
        }
    }
}

int main() {
    char input[3];

    scanf("%s", input);

    row = input[1] - '0';
    col = input[0] - 'a' + 1;

    countCase();

    printf("%d", cnt);

    return 0;
}