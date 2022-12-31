arr = [1, 2, 3, 4, 5]

arr.sort()

print(arr)

arr.sort(reverse=True)

print(arr)

arr2 = [[4, 1], [4, 3], [3, 2]]

arr2.sort(key=lambda x: (x[0], x[1]))

print(arr2)

arr2.sort(key=lambda x: (-x[0], -x[1]))

print(arr2)
