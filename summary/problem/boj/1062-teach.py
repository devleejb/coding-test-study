from itertools import combinations

N, K = map(int, input().split())
word_list = [input() for _ in range(N)]
arr = [1, 3, 4, 5, 6, 7, 9, 10, 11, 12,
       14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25]

result = 0


def check_readable(word, alpha_list):
    for char in word[4:len(word) - 4]:
        if (not alpha_list[ord(char) - 97]):
            return False
    return True


if (K < 5):
    print(0)
else:
    combination_list = list(combinations(arr, K - 5))
    for comb in combination_list:
        tmp_max = 0
        comb = list(comb) + [0, 2, 8, 13, 19]
        alpha_list = [i in comb for i in range(26)]

        for word in word_list:
            if (check_readable(word, alpha_list)):
                tmp_max += 1

        result = max(tmp_max, result)

    print(result)
