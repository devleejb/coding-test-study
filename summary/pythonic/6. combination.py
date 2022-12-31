from itertools import combinations, combinations_with_replacement

arr = [1, 2, 3, 4, 5]

print(list(combinations(arr, 3)))

print(list(combinations_with_replacement(arr, 3)))
