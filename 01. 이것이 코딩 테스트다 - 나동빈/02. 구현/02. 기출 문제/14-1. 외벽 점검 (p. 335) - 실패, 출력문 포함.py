# 14. 외벽 점검 (p. 335)
# https://programmers.co.kr/learn/courses/30/lessons/60062

def solution(n, weak, friends):
    friends.sort(reverse=True)
    len_friends = len(friends)
    print(f"** n: {n}개의 원형 레스토랑")
    print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
    print(f"** 취약점 리스트(weak): {weak}")

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
    print(f"** 취약점 사이의 거리 리스트의 최초합(sum_dist): {sum_dist}")
    answer = -1

    # 1.
    sum_friends = 0
    for i in range(len_friends):
        print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
        max_dist = -1
        for j in range(len_dist):
            if dist[j][1] == 0:
                if max_dist == -1:
                    max_dist = dist[j][0]
                elif max_dist < dist[j][0]:
                    max_dist = dist[j][0]
        num_max = dist.count([max_dist, 0])
        print(f" (i={i}) dist 리스트의 최댓값(max_dist): {max_dist} ({num_max}개)")
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
                print(f"  (j={j}) max값의 인덱스(index_max): {index_max}")
                print(f"  (j={j}) max값 주변의 인덱스(index_around_max): {index_around_max}")
        # 3.
        for j in range(len_dist):
            if j == index_max:
                dist[j][1] = 1
            elif j in index_around_max:
                dist[j][1] = 2
        sum_dist -= dist[index_max][0]
        sum_friends += friends[i]
        print(f"max값을 제외한 dist리스트의 합(sum_dist): {sum_dist}")
        print(f"{i + 1}명, 친구의 거리의 합(sum_friends): {sum_friends}")
        if sum_dist <= sum_friends:
            answer = i + 1
            break
        print("------------------------------")

    return answer

# Input
N1 = 12
WEAK1 = [1, 5, 6, 10]
DIST1 = [1, 2, 3, 4]
# 2

N2 = 12
WEAK2 = [1, 3, 4, 9, 10]
DIST2 = [3, 5, 7]
# 1

N3 = 200
WEAK3 = [0, 10, 50, 80, 120, 160]
DIST3 = [1, 10, 5, 40, 30]
# 3

N4 = 16
WEAK4 = [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15]
DIST4 = [4, 2, 1, 1]
# 4

N5 = 50
WEAK5 = [1]
DIST5 = [6]
# 1

N6 = 12
WEAK6 = [10, 0]
DIST6 = [1, 2]
# 1

N7 = 150
WEAK7 = [0, 40, 70, 110, 120, 130]
DIST7 = [10, 20, 15, 20]
# 안될듯?

# Output
print(solution(N4, WEAK4, DIST4))