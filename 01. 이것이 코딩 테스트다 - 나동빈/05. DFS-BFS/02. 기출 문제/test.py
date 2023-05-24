from collections import deque
list_a = [[1]]
i = deque(list_a)
i.popleft()

if not i:
    print(123)