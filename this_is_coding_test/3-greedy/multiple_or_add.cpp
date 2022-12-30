#include <iostream>
#include <string>

using namespace std;

string S;
int maxSum;

void calculateSum() {
    maxSum = S[0] - '0';

    for (int i = 1; i < S.size(); ++i) {
        if (maxSum + (S[i] - '0') > maxSum * (S[i] - '0')) {
            maxSum += S[i] - '0';
        } else {
            maxSum *= S[i] - '0';
        }
    }
}

int main(int argc, char const *argv[]) {
    cin >> S;

    calculateSum();

    cout << maxSum;

    return 0;
}
