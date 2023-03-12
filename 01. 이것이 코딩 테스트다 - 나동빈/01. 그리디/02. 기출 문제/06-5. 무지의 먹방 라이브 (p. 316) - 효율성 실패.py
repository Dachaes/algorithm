# 06. 무지의 먹방 라이브 (p. 316)
# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    len_time = len(food_times)                      # (ex: [4 4 4 7 7 9] -> 6)
    previous_time = 0

    # 0. 먹을 음식이 없을 때 + 먹을 시간 k가 너무 많아서 결국 다 먹게 될 때
    if k >= sum(food_times):
        return -1
    # 1, 2
    for j in range(min(food_times), max(food_times) + 1):
        current_time = j
        cnt = food_times.count(current_time)
        if cnt > 0:
            time = current_time - previous_time
            # 1. 시간 k가 충분할 때 (ex: [4 4 4 7 7 9], k = 25 -> [0 0 0 3 3 5], k = 1)
            if k >= (time * len_time):                  # 1-1. k초에서 묶음으로 빼기
                k -= (time * len_time)
                len_time -= cnt
                previous_time = current_time

            # 2. 시간 k가 충분하지 않아서 묶음으로 뺄셈이 되지 않을 때 (ex: [4 4 4 7 7 9], k = 10)
            else:
                k = k % len_time                        # 2-1. 마지막으로 먹은 음식 찾기 (k = 10 % 6 -> 4)
                if k == 0:                              # 2-2. 다음으로 먹을 음식 순서를 order에 저장
                    order = 1
                else:
                    order = k + 1
                for i in range(len(food_times)):
                    if food_times[i] >= current_time:
                        order -= 1
                    if order == 0:
                        return i + 1


# Input
food_times_list = list(map(int, input().split()))
K = int(input())

# Output
print(solution(food_times_list, K))