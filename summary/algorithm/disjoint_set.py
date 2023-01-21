def find_parent(parent_list, x):
    if (parent_list[x] != x):
        parent_list[x] = find_parent(parent_list, parent_list[x])
    return parent_list[x]


def union_parent(parent_list, a, b):
    a = find_parent(parent_list, a)
    b = find_parent(parent_list, b)

    if (a < b):
        parent_list[b] = a
    else:
        parent_list[a] = b
