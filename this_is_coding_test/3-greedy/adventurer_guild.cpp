#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int N, cnt, idx;
vector<int> score;

void countTeam() {
    int member = 0;

    for (int i = 0; i < score.size(); ++i) {
        member += 1;

        if (member >= score[i]) {
            ++cnt;
            member = 0;
        }
    }
}

int main() {
    int tmp;

    scanf("%d", &N);

    for (int i = 0; i < N; ++i) {
        scanf("%d", &tmp);

        score.push_back(tmp);
    }

    idx = score.size() -1;

    sort(score.begin(), score.end());

    countTeam();

    printf("%d", cnt);

    return 0;
}