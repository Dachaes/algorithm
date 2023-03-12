# 06. 무지의 먹방 라이브 (p. 316)
# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    # n 번째 음식을 먹을 차례 (0 ~ len(food_times))
    n = 0
    while k != 0:
        for i in range(len(food_times)):
            if food_times[i] > 0:
                food_times[i] -= 1
                k -= 1
                n = i + 1

    # 네트워크 장애로 인해 식사 중지!
    # n 번째 음식을 먹을 차례인데
    # 만약 이전에 먹었던 음식이 맨 마지막 음식이면 제일 처음 음식을 먹을 차례
    if n == len(food_times):
        n = 0

    # 만약 n 번째 음식이 남아 있지 않다면
    if food_times[n] == 0:
        temp = n
        # 다음 음식이 남아 있는지, 음식 리스트 끝까지 체크
        for i in range(n + 1, len(food_times)):
            if food_times[i] != 0:
                n = i
                break
        # 음식 리스트 끝까지 체크했음에도 남아 있는 음식이 없다면
        if temp == n:
            # 음식 리스트 처음부터 n 번째 음식까지 다시 체크
            for i in range(0, n):
                if food_times[i] != 0:
                    n = i
                    break
        # 음식 리스트의 처음부터 끝까지 체크했음에도 남아 있는 음식이 없다면
        if temp == n:
            n = -2

    return n + 1

# Input
food_times_list = list(map(int, input().split()))
K = int(input())

# Output
print(solution(food_times_list, K))
