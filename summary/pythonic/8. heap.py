import heapq

heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)

print(heap)

print(heapq.heappop(heap))
