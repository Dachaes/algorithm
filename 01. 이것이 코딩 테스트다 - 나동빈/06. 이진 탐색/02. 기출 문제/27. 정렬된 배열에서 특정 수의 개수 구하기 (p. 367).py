# 27. 정렬된 배열에서 특정 수의 개수 구하기 (p. 367)
import sys

# Input
n, x = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))


def find_number(start, mid, end):
    min_index, max_index, count = -1, -1, -1
    # 1. min_index 찾기
    while start <= end:
        if x <= numbers[mid]:
            if x == numbers[mid]:
                min_index = mid
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2

    # 2. max_index 찾기
    start, end = mid, n - 1
    while start <= end:
        if x < numbers[mid]:
            end = mid - 1
        else:
            if x == numbers[mid]:
                max_index = mid
            start = mid + 1
        mid = (start + end) // 2

    # 3. 특정 숫자(x)의 개수 도출
    if min_index != -1 and max_index != -1:
        count = max_index - min_index + 1
    return count


answer = find_number(0, (n - 1) // 2, n - 1)
print(answer)

# 7 2
# 1 1 2 2 2 2 3
# res = 4

# 7 4
# 1 1 2 2 2 2 3
# res = -1

# 9 5
# 1 1 2 2 3 3 4 4 5
# res = 1

# 6 2
# 2 2 2 2 2 2
# res = 6