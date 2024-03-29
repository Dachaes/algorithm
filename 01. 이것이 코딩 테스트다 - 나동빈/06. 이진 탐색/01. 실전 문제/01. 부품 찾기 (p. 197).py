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
        return False
    if mid == n - 1 and target != components[n - 1]:
        return False

    if target == components[mid]:
        return True
    elif target < components[mid]:
        return find_component(target, (mid - 1) // 2, start, mid - 1)
    elif components[mid] < target:
        return find_component(target, ((mid + 1) + end) // 2, mid + 1, end)


for request in requests:
    if find_component(request, (n - 1) // 2, 0, n - 1):
        answers.append('yes')
    else:
        answers.append('no')

for answer in answers:
    print(answer, end=" ")


# 5
# 8 3 7 9 2
# 3
# 5 7 9
# res = no yes yes

# 5
# 8 3 7 9 2
# 3
# 1 4 5
# res = no no no