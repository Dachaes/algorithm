# 02. 떡볶이 떡 만들기 (p. 201)
import sys

# Input
n, request = map(int, sys.stdin.readline().split())
tteoks = list(map(int, sys.stdin.readline().split()))
the_longest_tteok = max(tteoks)


def cut_tteoks(start, mid, end):
    len_tteok, left_over, = -1, -1
    while True:
        temp_left_over = 0
        # 1. 종료 조건
        if start > end:
            return len_tteok

        # 2-1. 떡 자르기 조건
        temp_len_tteok = mid
        for tteok in tteoks:
            if temp_len_tteok < tteok:
                temp_left_over += tteok - temp_len_tteok

        if temp_left_over >= request:
            # 2-2. 값 저장 조건 -> 손님에게 줄 떡(left_over)이 충분 + 기존보다 많은 길이의 떡(len_tteok)을 남김
            if len_tteok == left_over == -1:
                len_tteok = temp_len_tteok
                left_over = temp_left_over
            elif len_tteok < temp_len_tteok:
                len_tteok = temp_len_tteok
                left_over = temp_left_over
            # 3-1. 탐색 조건 -> 손님에게 줄 떡(left_over)이 충분하니, 남기는 떡의 길이(len_tteok)를 더 늘린다.
            start = mid + 1
            mid = (start + end) // 2

        # 3-2. 탐색 조건 -> 손님에게 줄 떡(left_over)이 부족하니, 남기는 떡의 길이(len_tteok)를 더 줄인다.
        else:
            end = mid - 1
            mid = (start + end) // 2


answer = cut_tteoks(0, (n - 1) // 2, the_longest_tteok - 1)
print(answer)

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