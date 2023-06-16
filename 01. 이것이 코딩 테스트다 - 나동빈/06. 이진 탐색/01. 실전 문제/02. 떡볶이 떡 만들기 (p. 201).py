# 02. 떡볶이 떡 만들기 (p. 201)
import sys

# Input
n, request = map(int, sys.stdin.readline().split())
tteoks = list(map(int, sys.stdin.readline().split()))
tteoks.sort()


def cut_tteoks(array, mid, start, end):
    # 이진 탐색 조건
    global target
    while True:
        mid1 = mid
        mid2 = mid + 1
        # print(f"target: {target} --> mid1: {mid1}, mid2: {mid2}")
        # 1. 종료 조건
        if mid1 != -1 and mid2 != n:
            if array[mid1] <= target <= array[mid2] or array[0] <= target:
                target = mid2
                break
            elif array[n - 1] <= target:
                target = -1
                break
        else:
            target = -1
            break

        # 2. 탐색 조건
        if array[mid2] < target:
            start = mid + 1
            mid = (start + end) // 2
        elif target < array[mid1]:
            end = mid - 1
            mid = (start + end) // 2

    # 떡 자르기 조건
    global left_over
    if target != -1:
        for i in range(target, end):
            left_over += array[i] - target


target = tteoks[-1] - 1
while True:
    left_over = 0
    if left_over >= request:
        break
    cut_tteoks(tteoks, (n - 1) // 2, 0, n - 1)
    target -= 1

print(left_over)

# 4 6
# 19 15 10 17
# res = 15

# 5 11
# 10 11 12 13 14
# res = 9

# 1 1
# 1
# res = 0

# 4 7
# 19 15 10 17
# res = 14

# 4 10
# 19 15 10 17
# res = 13