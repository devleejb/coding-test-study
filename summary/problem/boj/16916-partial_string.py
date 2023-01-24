def make_table(pattern):
    pattern_size = len(pattern)
    table = [0] * pattern_size

    j = 0

    for i in range(1, pattern_size):
        while (j > 0 and pattern[i] != pattern[j]):
            j = table[j - 1]

        if (pattern[i] == pattern[j]):
            table[i] = j = j + 1

    return table


def kmp(parent, pattern):
    table = make_table(pattern)
    parent_size = len(parent)
    pattern_size = len(pattern)
    j = 0
    for i in range(parent_size):
        while (j > 0 and parent[i] != pattern[j]):
            j = table[j - 1]

        if (parent[i] == pattern[j]):
            if (j == pattern_size - 1):
                return 1
            else:
                j = j + 1
    return 0


parent = input()
pattern = input()
print(kmp(parent, pattern))
