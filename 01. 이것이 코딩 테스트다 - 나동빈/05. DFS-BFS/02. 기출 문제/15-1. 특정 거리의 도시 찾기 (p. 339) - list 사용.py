# 15. 특정 거리의 도시 찾기 (p. 339)
# https://www.acmicpc.net/problem/18352
# list 사용 / 단방향 도로 입력을 그대로 사용
import sys

# Input
num_city, num_street, final_dist, start = map(int, sys.stdin.readline().split())
streets = []
for _ in range(num_street):
    streets.append(list(map(int, sys.stdin.readline().split())))

dist_list = [-1] * (num_city + 1)   # 최단 거리를 저장할 리스트
pos_city = [start]                  # 현재 위치의 도시

res = []                            # 원하는 최단 거리의 도시를 저장할 리스트
dist = 0                            # 현재 확인하고 있는 최단 거리
while pos_city:
    # 1. 현재 위치의 도시를 pos_list에 저장한다.
    pos_list = pos_city
    print(f"pos_list: {pos_city}, dist: {dist}")
    # 2.
    pos_city = []
    for pos in pos_list:
        # 2-1. 해당 도시를 간 적이 아직 없다면, dist_list에 해당 도시의 최단 거리를 저장한다.
        if dist_list[pos] == -1:
            dist_list[pos] = dist
            if dist == final_dist:
                res.append(pos)
            # 2-2. 다음 위치(다음 최단 거리)의 도시 리스트 생성한다.
            for street in streets:
                if pos == street[0] and street[1] not in pos_city:
                    pos_city.append(street[1])

    print(f" dist_list: {dist_list}")
    # 3. 다음 최단 거리 확인
    dist += 1

    # 4. 원하는 최단 거리(final_dist) 값만큼 현재 확인하고 있는 최단 거리(dist)가 증가했다면,
    # 원하는 최단 거리(final_dist)의 도시를 저장할 리스트 res를 채우고, while 문을 나간다.
    if dist > final_dist:
        break

# 5. res가 존재하면 해당 요소들을 출력하고, 아니면 -1을 출력한다.
res.sort()
if res:
    for r in res:
        print(r)
else:
    print(-1)