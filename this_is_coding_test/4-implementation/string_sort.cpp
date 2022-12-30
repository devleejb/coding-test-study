#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int number;
vector<char> character;

int main() {
    char tmpChar;

    scanf("%c", &tmpChar);

    while (tmpChar != '\n')
    {
        if (tmpChar >= 'A' && tmpChar <= 'Z') {
            character.push_back(tmpChar);
        } else {
            number += tmpChar - '0';
        }

        scanf("%c", &tmpChar);
    }

    sort(character.begin(), character.end());

    for (int i = 0; i < character.size(); ++i) {
        printf("%c", character[i]);
    }

    printf("%d", number);

    return 0;
}