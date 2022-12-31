arr = [1, 1, 1, 2, 3, 4, 5]

print(list(set(arr)))

arr2 = [[1, 2], [1, 2], [1, 3], [4, 5]]

print(list(set(map(tuple, arr2))))
