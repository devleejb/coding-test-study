from itertools import permutations, product

arr = [1, 2, 3, 4, 5]

print(list(permutations(arr, 3)))

print(list(product(arr, repeat=3)))
