# 28. 고정점 찾기 (p. 368)
import sys

# Input
n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))


def find_point(start, mid, end):
    while start <= end:
        if numbers[mid] == mid:
            return mid
        elif numbers[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2

    return -1

answer = find_point(0, (n - 1) // 2, n - 1)
print(answer)

# 5
# -15 -6 1 3 7
# res = 3

# 7
# -15 -4 2 8 9 13 15
# res = 2

# 7
# -15 -4 3 8 9 13 15
# res = -1