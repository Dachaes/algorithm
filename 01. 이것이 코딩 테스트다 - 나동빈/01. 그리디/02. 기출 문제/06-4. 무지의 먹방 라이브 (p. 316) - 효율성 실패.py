# 06. 무지의 먹방 라이브 (p. 316)
# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    len_time = len(food_times)                      # (ex: [4 4 4 7 7 9] -> 6)
    current_time = min(food_times)                  # (ex: [4 4 4 7 7 9] -> 4)

    # 0. 먹을 음식이 없을 때 + 먹을 시간 k가 너무 많아서 결국 다 먹게 될 때
    if k >= sum(food_times):
        return -1
    while True:
        # 1. 시간 k가 충분할 때 (ex: [4 4 4 7 7 9], k = 25 -> [0 0 0 3 3 5], k = 1)
        if k >= (current_time * len_time):
            k -= (current_time * len_time)          # 1-1. k초에서 묶음으로 빼기
            len_time, find_min = 0, 0
            for i in range(len(food_times)):
                if food_times[i] >= current_time:   # 1-2. 사용한 food_list 갱신 (food_list = [0 0 0 3 3 5])
                    food_times[i] -= current_time
                if food_times[i] > 0:
                    len_time += 1                   # 1-3. 남아있는 food_time 길이 체크 (len_time = 3)
                    if find_min == 0:               # 1-4. 다음으로 가장 작은 food_time 찾기 (find_min = 3)
                        find_min = food_times[i]
                    else:
                        temp = food_times[i]
                        if find_min > temp:
                            find_min = temp
            current_time = find_min
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