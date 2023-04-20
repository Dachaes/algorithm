# 15. 특정 거리의 도시 찾기 (p. 339)
# https://www.acmicpc.net/problem/18352
# deque 사용 / 입력 받을 때, 단방향 도로를 인접 리스트로 정리해서 사용
from collections import deque
import sys

# Input
num_city, num_street, final_dist, start = map(int, sys.stdin.readline().split())
streets = [[] for _ in range(num_city + 1)]
for _ in range(num_street):
    data = list(map(int, sys.stdin.readline().split()))
    if data[1] not in streets[data[0]]:
        streets[data[0]].append(data[1])
print(f"streets: {streets}")

dist_list = [-1] * (num_city + 1)   # 최단 거리를 저장할 리스트
pos_city = deque([[start]])         # 현재 위치의 도시

res = []                            # 원하는 최단 거리의 도시를 저장할 리스트
dist = 0                            # 현재 확인하고 있는 최단 거리
while pos_city:
    # 1. 현재 위치의 도시를 pos_list에 저장한다.
    pos_list = pos_city.popleft()
    print(f"pos_list: {pos_list}, dist: {dist}")
    # 2.
    temp_city = []
    for pos in pos_list:
        print(f"  pos: {pos} 확인 중!")
        # 2-1. 해당 도시를 간 적이 아직 없다면, dist_list에 해당 도시의 최단 거리를 저장한다.
        if dist_list[pos] == -1:
            dist_list[pos] = dist
            if dist == final_dist:
                res.append(pos)
            # 2-2. 다음 위치(다음 최단 거리)의 도시 리스트 생성한다.
            for city in streets[pos]:
                print(f"  streets[pos]: {streets[pos]} 확인 중!")
                if city not in pos_city:
                    temp_city.append(city)
                print(f"  temp_city: {temp_city}")
    pos_city.append(temp_city)
    print(f"   pos_city: {pos_city}")
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