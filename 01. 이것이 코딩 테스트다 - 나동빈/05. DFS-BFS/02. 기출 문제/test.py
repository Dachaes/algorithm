from collections import deque
from copy import deepcopy

numbers = [1, 2, 3, 4]
deq_numbers = deque(numbers)
new_numbers = deepcopy(deq_numbers)

new_numbers.popleft()
print(new_numbers)