from sys import stdin

input = stdin.readline

V, E = map(int, input().split())
edge_list = [list(map(int, input().split())) for _ in range(E)]
parent_list = [i for i in range(V + 1)]
result = 0

edge_list.sort(key=lambda x: x[2])


def find_parent(parent_list, x):
    if (x != parent_list[x]):
        parent_list[x] = find_parent(parent_list, parent_list[x])
    return parent_list[x]


def union_parent(parent_list, a, b):
    a = find_parent(parent_list, a)
    b = find_parent(parent_list, b)

    if (a < b):
        parent_list[b] = a
    else:
        parent_list[a] = b


for edge in edge_list:
    start, end, cost = edge
    parent_start = find_parent(parent_list, start)
    parent_end = find_parent(parent_list, end)

    if (parent_start != parent_end):
        union_parent(parent_list, parent_start, parent_end)
        result += cost


print(result)
