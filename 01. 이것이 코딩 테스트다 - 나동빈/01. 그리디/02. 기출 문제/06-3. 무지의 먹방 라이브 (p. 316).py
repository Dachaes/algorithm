# 06. 무지의 먹방 라이브 (p. 316)
# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    # 0. 먹을 음식이 없을 때 + 먹을 시간 k가 너무 많아서 결국 다 먹게 될 때
    if k >= sum(food_times):
        return -1

    # 1. 먹을 음식이 있을 때
    max_time = max(food_times)
    for i in range(1, max_time + 1):
        # 1. i초 기준으로 남은 음식의 갯수(cnt) 체크
        cnt = 0
        for food_time in food_times:
            if food_time >= i:
                cnt += 1

        # 1-1. 먹을 시간 k가 충분할 때
        if k >= cnt:
            k -= cnt

        # 1-2. 먹을 시간 k가 충분하지 않을 때
        else:
            for j in range(0, len(food_times)):
                if food_times[j] >= i:
                    k -= 1
                if k == -1:
                    return j + 1
    return 1

# Input
food_times_list = list(map(int, input().split()))
K = int(input())

# Output
print(solution(food_times_list, K))