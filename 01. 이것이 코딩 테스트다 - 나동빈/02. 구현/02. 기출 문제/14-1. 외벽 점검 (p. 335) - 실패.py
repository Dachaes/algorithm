# 14. 외벽 점검 (p. 335)
# https://programmers.co.kr/learn/courses/30/lessons/60062

def solution(n, weak, friends):
    friends.sort(reverse=True)
    len_friends = len(friends)

    dist = []
    # dist: 취약점 사이의 거리를 저장한 리스트
    sum_dist = 0
    temp = weak[-1]
    for i in range(len(weak)):
        if weak[i] >= temp:
            dist.append([weak[i] - temp, 0])
            sum_dist += (weak[i] - temp)
        else:
            dist.append([weak[i] - temp + n, 0])
            sum_dist += (weak[i] - temp + n)
        temp = weak[i]
    len_dist = len(dist)

    answer = -1
    # 1.
    sum_friends = 0
    for i in range(len_friends):
        max_dist = -1
        for j in range(len_dist):
            if dist[j][1] == 0:
                if max_dist == -1:
                    max_dist = dist[j][0]
                elif max_dist < dist[j][0]:
                    max_dist = dist[j][0]
        # 2.
        index_max = -1
        value_around_max, index_around_max = [], []
        for j in range(len_dist):
            temp_value_around_max, temp_index_around_max = [], []
            if dist[j] == [max_dist, 0]:
                if not value_around_max:
                    index_max = j
                    value_around_max.append(dist[(j - 1) % len_dist][0])
                    value_around_max.append(dist[(j + 1) % len_dist][0])
                    index_around_max.append((j - 1) % len_dist)
                    index_around_max.append((j + 1) % len_dist)
                else:
                    temp_index_max = j
                    temp_value_around_max.append(dist[(j - 1) % len_dist][0])
                    temp_value_around_max.append(dist[(j + 1) % len_dist][0])
                    temp_index_around_max.append((j - 1) % len_dist)
                    temp_index_around_max.append((j + 1) % len_dist)
                    if sum(temp_value_around_max) < sum(value_around_max):
                        index_max = temp_index_max
                        index_around_max = temp_index_around_max
        # 3.
        for j in range(len_dist):
            if j == index_max:
                dist[j][1] = 1
            elif j in index_around_max:
                dist[j][1] = 2
        sum_dist -= dist[index_max][0]
        sum_friends += friends[i]
        if sum_dist <= sum_friends:
            answer = i + 1
            break

    return answer

# Input
N1 = 12
WEAK1 = [1, 5, 6, 10]
DIST1 = [1, 2, 3, 4]

N2 = 12
WEAK2 = [1, 3, 4, 9, 10]
DIST2 = [3, 5, 7]

# Output
print(solution(N2, WEAK2, DIST2))