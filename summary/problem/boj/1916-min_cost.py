from sys import maxsize

N = int(input())
M = int(input())
dis_list = [maxsize] * (N + 1)
visited_list = [False] * (N + 1)
edge_list = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    edge_list[start].append((end, cost))

start, end = map(int, input().split())


def get_min_node(node):
    min_node = -1
    min_dis = maxsize

    for i in range(1, N + 1):
        if (not visited_list[i] and min_dis > dis_list[i]):
            min_node = i
            min_dis = dis_list[i]

    return min_node


def dijkstra():
    visited_list[start] = True
    dis_list[start] = 0

    for edge in edge_list[start]:
        dis_list[edge[0]] = min(edge[1], dis_list[edge[0]])

    now = start

    for _ in range(N - 1):
        now = get_min_node(now)
        visited_list[now] = True

        for edge in edge_list[now]:
            dis_list[edge[0]] = min(dis_list[edge[0]], dis_list[now] + edge[1])


dijkstra()

print(dis_list[end])
