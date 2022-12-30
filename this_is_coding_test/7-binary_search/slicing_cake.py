from symbol import sliceop


N, M = map(int, input().split())
cake_list = list(map(int, input().split()))

max_in_list = max(cake_list)
min_val = 0


def slice_cake(h):
    sliced_height = 0

    for height in cake_list:
        if (height > h):
            sliced_height += height - h

    return sliced_height


def binary_search(start, end):
    if (start > end):
        return None

    global min_val

    mid = (start + end) // 2

    sliced_height = slice_cake(mid)

    if (sliced_height == M):
        min_val = mid
    elif (sliced_height > M):
        min_val = mid
        binary_search(mid + 1, end)
    else:
        binary_search(start, mid - 1)


binary_search(0, max_in_list)
print(min_val)
