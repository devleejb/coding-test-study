from collections import deque

deq = deque([1, 2, 3, 4, 5])

deq.appendleft(0)
deq.append(10)

print(deq)

print(deq.popleft())
print(deq.pop())
print(deq)

deq.rotate(1)
print(deq)
