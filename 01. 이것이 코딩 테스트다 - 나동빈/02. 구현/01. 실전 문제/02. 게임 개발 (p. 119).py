# 02. 게임 개발 (p. 119)

# Input
map_size = list(map(int, input().split()))              # N x M 크기의 맵
character = list(map(int, input().split()))             # (x 좌표, y 좌표, 방향)
map_shape = []                                          # 0: 육지, 1: 바다
for i in range(map_size[0]):
    map_shape.append(list(map(int, input().split())))

direction = character[2]                        # 캐릭터가 보는 방향
location = (character[0], character[1])         # 캐릭터가 있는 위치
routes = [(-1, 0), (0, 1), (1, 0), (0, -1)]     # [북(0), 동(1), 남(2), 서(3)]

visited_location = [location]
while True:
    previous_location = location                # 캐릭터의 이전 위치 저장
    for i in range(1, len(routes) + 1):
        direction -= 1                          # 캐릭터의 방향 저장
        if direction < 0:                       # 캐릭터의 방향 조정
            direction += 4
        next_location = (location[0] + routes[direction][0], location[1] + routes[direction][1])    # 캐릭터의 다음 위치 저장
        # 1. 다음 위치가 맵 밖을 벗어나지 않고, 육지라면 이미 간 곳인지 확인한다.
        if (0 <= next_location[0] < map_size[0]) and (0 <= next_location[1] < map_size[1]) and (map_shape[next_location[0]][next_location[1]]) == 0:
            # 2. 해당 위치가 아직 가보지 않은 곳이면, 이 위치를 다음 위치로 변경하고 for 문을 나간다.
            # 만약 가본 곳이라면, for문의 시작점으로 돌아가서 캐릭터의 방향을 돌리고, 다시 다음 위치를 탐색한다.
            if next_location not in visited_location:
                previous_location = location
                location = next_location
                visited_location.append(location)
                break

    # 3. 네 방향 모두 갔던 곳이라면 캐릭터의 현재 위치의 바로 등 뒤의 위치를 확인해 준다.
    if previous_location == location:
        next_location = (location[0] - routes[direction][0], location[1] - routes[direction][1])    # 캐릭터의 다음 위치 저장
        # 3-1. 그 위치가 바다라면, 반복문을 완전히 종료한다.
        if (map_shape[next_location[0]][next_location[1]]) == 1:
            break
        # 3-2. 그게 아니라면 캐릭터를 다음 위치로 변경하고, While 문의 시작점으로 돌아간다.
        elif (0 <= next_location[0] < map_size[0]) and (0 <= next_location[1] < map_size[1]):
            previous_location = location
            location = next_location
            if next_location not in visited_location:
                visited_location.append(location)

num = len(visited_location)
print(f"방문한 칸: {visited_location}\n방문한 수: {num}번")