# 01. 부품 찾기 (p. 197)
import sys

# Input
n = int(sys.stdin.readline().rstrip())
components = list(map(int, sys.stdin.readline().split()))
components.sort()
m = int(sys.stdin.readline().rstrip())
requests = list(map(int, sys.stdin.readline().split()))

answers = []


def find_component(target, mid, start, end):
    if mid == 0 and target != components[0]:
        answers.append('no')
        return False
    if mid == n - 1 and target != components[n - 1]:
        answers.append('no')
        return False

    if target == components[mid]:
        answers.append('yes')
        return True
    elif target < components[mid]:
        find_component(target, (mid - 1) // 2, start, mid - 1)
    elif components[mid] < target:
        find_component(target, ((mid + 1) + end) // 2, mid + 1, end)


for request in requests:
    find_component(request, (n - 1) // 2, 0, n - 1)

for answer in answers:
    print(answer, end=" ")

# 5
# 8 3 7 9 2
# 3
# 5 7 9
# no yes yes

# 5
# 8 3 7 9 2
# 3
# 1 4 5
# no no no