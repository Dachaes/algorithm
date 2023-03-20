# 13. 치킨 배달 (p. 332)
# https://www.acmicpc.net/problem/15686
from itertools import combinations

# Input
len_city, num_restaurants = map(int, input().split())
city = []               # 0: 빈칸, 1: 집, 2: 치킨집
for _ in range(len_city):
    city.append(list(map(int, input().split())))

# 도시 내의 집과 치킨집의 좌표를 각각의 리스트에 저장
houses = []
restaurants = []
for i in range(len_city):
    for j in range(len_city):
        if city[i][j] == 1:
            houses.append([i + 1, j + 1])
        elif city[i][j] == 2:
            restaurants.append([i + 1, j + 1])

# 남길 치킨집의 수(num_restaurants = M)의 경우의 수를 모두 all_cases_of_chosen_restaurants에 저장
all_cases_of_chosen_restaurants = list(combinations(restaurants, num_restaurants))

chicken_streets = []
for chosen_restaurants in all_cases_of_chosen_restaurants:
    sum_of_chicken_street = 0
    # 1. 집 하나를 고른다.
    for house in houses:
        chicken_street = 0
        hou_x = house[0]
        hou_y = house[1]
        # 2. M개를 치킨집을 고르는 경우의 수 중 하나에서, 가장 가까운 거리의 치킨집의 치킨 거리를 계산한다.
        # 즉, 1에서 고른 집의 치킨 거리(최솟값)
        for i in range(num_restaurants):
            res_x = chosen_restaurants[i][0]
            res_y = chosen_restaurants[i][1]
            if chicken_street == 0 or chicken_street > abs(res_x - hou_x) + abs(res_y - hou_y):
                chicken_street = abs(res_x - hou_x) + abs(res_y - hou_y)
        # 3. 모든 집의 치킨 거리를 합하여 도시의 치킨거리를 계산한다.
        sum_of_chicken_street += chicken_street
    # 4. 모든 경우의 수의 도시의 치킨 거리를 chichen_streets라는 리스트에 넣는다.
    chicken_streets.append(sum_of_chicken_street)
# 5. M개의 치킨집만 남겼을 때, 도시의 치킨 거리의 최솟값을 결과값에 넣는다.
res = min(chicken_streets)
print(res)