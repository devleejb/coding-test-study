#include <stdio.h>

using namespace std;

int N, cnt, hour, min, sec;

void countTime() {
    while (!(hour == N && min == 59 && sec == 59)) {
        ++sec;

        if (sec == 60) {
            ++min;
            sec = 0;

            if (min == 60) {
                ++hour;
                min = 0;
            }
        }

        if (hour / 10 == 3 || hour % 10 == 3 || min / 10 == 3 || min % 10 == 3 || sec / 10 == 3 || sec % 10 == 3) {
            ++cnt;
        }
    }
}

int main(int argc, char const *argv[]) {
    scanf("%d", &N);

    countTime();

    printf("%d", cnt);

    return 0;
}