# 06. 무지의 먹방 라이브 (p. 316)
# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    n = 0                               # n 번째 음식을 먹을 차례 (리스트 인덱스 기준! -> 0 ~ len(food_times))
    len_food_times = len(food_times)    # food_times 리스트 길이
    count_0 = food_times.count(0)       # food_times 리스트에 0이 몇 개?

    # 0. 먹을 음식이 없을 때
    if len_food_times == count_0:
        return -1

    # 1. 식사 중!
    while k > 0:
        # 1-1. 먹을 횟수 k가 충분하여 food_times 리스트를 한 바퀴(처음부터 끝까지)씩 돌 수 있을 때
        # (이 경우엔 항상 마지막 음식까지 먹고 n = 0을 반환한다.)
        if k >= (len_food_times - count_0):
            for i in range(len_food_times):
                if food_times[i] > 0:
                    food_times[i] -= 1
                    k -= 1

        # 1-2. 먹을 횟수 k가 충분하지 않아서 food_times 리스트를 돌다가 중간에 멈춰야 할 때
        # (이 경우엔 네트워크 장애가 있을 때까지 음식을 먹고, 다음에 먹을 차례인 음식 번호 n을 반환한다.)
        # (반환한 음식 번호의 음식이 남아 있는 지는 아직 모른다.)
        else:
            for i in range(len_food_times):
                if food_times[i] > 0:
                    food_times[i] -= 1
                    k -= 1
                    n = i + 1
                if k == 0:
                    break
        count_0 = food_times.count(0)
        if len_food_times == count_0:
            return -1

    # 2. 네트워크 장애로 인해 식사 중지!
    # n 번째 음식을 먹을 차례인데, 만약 n 번째 음식이 남아 있지 않다면
    if food_times[n] == 0:
        temp = n
        # 2-1. 다음 음식이 남아 있는지, 음식 리스트 끝까지 체크
        for i in range(n + 1, len_food_times):
            if food_times[i] != 0:
                n = i
                break
        # 2-2. 음식 리스트 끝까지 체크했음에도 남아 있는 음식이 없다면
        # 음식 리스트 처음부터 n 번째 음식까지 다시 체크
        if temp == n:
            for i in range(0, n):
                if food_times[i] != 0:
                    n = i
                    break
    return n + 1

# Input
food_times_list = list(map(int, input().split()))
K = int(input())

# Output
print(solution(food_times_list, K))