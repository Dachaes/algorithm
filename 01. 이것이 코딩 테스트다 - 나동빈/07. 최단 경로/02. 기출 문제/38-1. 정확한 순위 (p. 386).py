# 38. 정확한 순위 (p. 386)
import sys
from collections import deque

# Input
num_students, num_comparisons = map(int, sys.stdin.readline().split())
comparisons = deque()
for _ in range(num_comparisons):
    comparisons.append(list(map(int, sys.stdin.readline().split())) + [False])

final_comparisons = []
while comparisons:
    temp = comparisons.popleft()
    check = True
    for i in range(len(comparisons)):
        comparison = comparisons[i]

        if temp[-2] == comparison[0]:
            temp[-1], comparison[-1] = True, True
            new_temp = temp[:-1] + comparison[1:-1] + [False]
            comparisons.append(new_temp)
    if not temp[-1]:
        final_comparisons.append(temp[:-1])

res = 0
for student in range(1, num_students + 1):
    count = set([])
    for final_comparison in final_comparisons:
        if student in final_comparison:
            count.update(final_comparison)
    if len(count) == num_students:
        res += 1

print(res)


# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4
# res = 1