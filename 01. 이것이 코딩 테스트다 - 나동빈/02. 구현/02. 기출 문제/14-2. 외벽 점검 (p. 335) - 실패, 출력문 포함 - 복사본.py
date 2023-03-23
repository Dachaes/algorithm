# 14. 외벽 점검 (p. 335)
# https://programmers.co.kr/learn/courses/30/lessons/60062

def solution(n, weak, friends):
    len_weak = len(weak)
    len_friends = len(friends)
    weak.sort()
    friends.sort(reverse=True)
    print(f"** n: {n}개의 원형 레스토랑")
    print(f"** 취약점 리스트(weak): {weak}")


    # dist: 취약점 사이의 거리를 저장한 리스트
    dist = []
    for i in range(len_weak):
        if i != (len_weak - 1):
            dist.append(weak[i + 1] - weak[i])
        else:
            dist.append(weak[0] - weak[i] + n)

    end_weak = [1] * len_weak
    answers = []
    for i in range(len_weak):
        start = i % len_weak        # 시작 지점
        end = (i - 2) % len_weak    # 완료 지점

        num_dist = start
        sum_dist = dist[start]
        end_num_dist = end

        num_friends = 0
        check = 0

        # check_weak, end_weak: 취약점을 모두 체크했는가?
        check_weak = [0] * len_weak

        print(f"-----------------i = {i}----------------")
        print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
        print(f"* 취약점 리스트(weak): {weak}")
        print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
        print(f"check_weak: {check_weak}")
        print(f"거리의 순서(num_dist): {num_dist}, 거리의 누적합(sum_dist): {sum_dist}")
        if num_friends < len_friends:
            print(f"친구의 순서(num_friends): {num_friends}, 해당 친구의 거리값: {friends[num_friends]}")
        else:
            print(f"탈출")

        while num_friends < len_friends:
            # 1. 해당 취약점과 그 다음 취약점 사이의 거리를 처음 체크한다면
            if check == 0:
                # 1-1. 가장 많이 걸을 수 있는 친구조차도 해당 거리를 가지 못하면,
                # 이전 취약점만 체크한 셈 치고, 그 다음 취약점과, 친구를 불러온다.
                if sum_dist > friends[num_friends]:
                    print("/check1-1/ 가장 많이 걸을 수 있는 친구조차도 해당 거리를 가지 못하면, 이전 취약점만 체크한 셈 치고, 그 다음 취약점과, 친구를 불러온다.")
                    check_weak[num_dist] = 1
                    print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
                    print(f"* 취약점 리스트(weak): {weak}")
                    print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
                    print(f"check_weak: {check_weak}")
                    if check_weak == end_weak:
                        break
                    num_dist = (num_dist + 1) % len_weak
                    sum_dist = dist[num_dist]
                    num_friends += 1
                    print(f"거리의 순서(num_dist): {num_dist}, 거리의 누적합(sum_dist): {sum_dist}")
                    if num_friends < len_friends:
                        print(f"친구의 순서(num_friends): {num_friends}, 해당 친구의 거리값: {friends[num_friends]}")
                    else:
                        print(f"탈출")

                # 1-2. 가장 많이 걸을 수 있는 친구가 해당 거리를 딱 맞춰서 갈 수 있다면, 그 다음 친구를 불러온다.
                elif sum_dist == friends[num_friends]:
                    print("/check1-2/ 가장 많이 걸을 수 있는 친구가 해당 거리를 딱 맞춰서 갈 수 있다면, 그 다음 친구를 불러온다.")
                    check_weak[num_dist] = 1
                    check_weak[(num_dist + 1) % len_weak] = 1
                    print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
                    print(f"* 취약점 리스트(weak): {weak}")
                    print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
                    print(f"check_weak: {check_weak}")
                    if check_weak == end_weak:
                        break
                    num_dist = (num_dist + 2) % len_weak
                    sum_dist = dist[num_dist]
                    num_friends += 1
                    print(f"거리의 순서(num_dist): {num_dist}, 거리의 누적합(sum_dist): {sum_dist}")
                    if num_friends < len_friends:
                        print(f"친구의 순서(num_friends): {num_friends}, 해당 친구의 거리값: {friends[num_friends]}")
                    else:
                        print(f"탈출")

                # 1-3. 가장 많이 걸을 수 있는 친구가 갈 수 있는 거리가 아직 남았다면, 다음 거리도 추가한다.
                else:
                    print("/check1-3/ 가장 많이 걸을 수 있는 친구가 갈 수 있는 거리가 아직 남았다면, 다음 거리도 추가한다.")
                    check = 1
                    check_weak[num_dist] = 1
                    check_weak[(num_dist + 1) % len_weak] = 1
                    print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
                    print(f"* 취약점 리스트(weak): {weak}")
                    print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
                    print(f"check_weak: {check_weak}")
                    if check_weak == end_weak:
                        break
                    num_dist = (num_dist + 1) % len_weak
                    sum_dist += dist[num_dist]
                    print(f"거리의 순서(num_dist): {num_dist}, 거리의 누적합(sum_dist): {sum_dist}")
                    if num_friends < len_friends:
                        print(f"친구의 순서(num_friends): {num_friends}, 해당 친구의 거리값: {friends[num_friends]}")
                    else:
                        print(f"탈출")

            # 2. 해당 취약점과 그 다음 취약점 사이의 거리를 체크한 적이 있다면
            else:
                # 2-1. 그 친구가 누적된 해당 거리를 가지 못하면, 그 친구는 직전 거리까지만 간다.
                # 거리 누적합은 다음 거리값으로 되돌리고, 다음 친구를 불러온다.
                if sum_dist > friends[num_friends]:
                    print("/check2-1/ 친구가 누적된 해당 거리를 가지 못하면, 그 친구는 직전 거리까지만 간다. 거리 누적합은 다음 거리값으로 되돌리고, 다음 친구를 불러온다.")
                    check = 0
                    num_dist = (num_dist + 1) % len_weak
                    sum_dist = dist[num_dist]
                    num_friends += 1
                    print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
                    print(f"* 취약점 리스트(weak): {weak}")
                    print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
                    print(f"check_weak: {check_weak}")
                    print(f"거리의 순서(num_dist): {num_dist}, 거리의 누적합(sum_dist): {sum_dist}")
                    if num_friends < len_friends:
                        print(f"친구의 순서(num_friends): {num_friends}, 해당 친구의 거리값: {friends[num_friends]}")
                    else:
                        print(f"탈출")


                # 2-2. 그 친구가 해당 거리를 딱 맞춰서 갈 수 있다면, 그 다음 친구를 불러온다.
                elif sum_dist == friends[num_friends]:
                    print("/check2-2/ 그 친구가 해당 거리를 딱 맞춰서 갈 수 있다면, 그 다음 친구를 불러온다.")
                    check = 0
                    check_weak[(num_dist + 1) % len_weak] = 1
                    print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
                    print(f"* 취약점 리스트(weak): {weak}")
                    print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
                    print(f"check_weak: {check_weak}")
                    if check_weak == end_weak:
                        break
                    num_dist = (num_dist + 2) % len_weak
                    sum_dist = dist[num_dist]
                    num_friends += 1
                    print(f"거리의 순서(num_dist): {num_dist}, 거리의 누적합(sum_dist): {sum_dist}")
                    if num_friends < len_friends:
                        print(f"친구의 순서(num_friends): {num_friends}, 해당 친구의 거리값: {friends[num_friends]}")
                    else:
                        print(f"탈출")

                # 2-3. 가장 많이 걸을 수 있는 친구가 갈 수 있는 거리가 아직 남았다면, 다음 거리도 추가한다.
                else:
                    print("/check2-3/ 가장 많이 걸을 수 있는 친구가 갈 수 있는 거리가 아직 남았다면, 다음 거리도 추가한다.")
                    check_weak[(num_dist + 1) % len_weak] = 1
                    print(f"** 친구별 이동할 수 있는 거리 리스트(friends): {friends}")
                    print(f"* 취약점 리스트(weak): {weak}")
                    print(f"* 취약점 사이의 거리 리스트(dist): {dist}")
                    print(f"check_weak: {check_weak}")
                    if check_weak == end_weak:
                        break
                    num_dist = (num_dist + 1) % len_weak
                    sum_dist += dist[num_dist]
                    print(f"거리의 순서(num_dist): {num_dist}, 거리의 누적합(sum_dist): {sum_dist}")
                    if num_friends < len_friends:
                        print(f"친구의 순서(num_friends): {num_friends}, 해당 친구의 거리값: {friends[num_friends]}")
                    else:
                        print(f"탈출")

        if check_weak == end_weak:
            answers.append(num_friends + 1)
        print("--------------------------------------")
        print(f"answers: {answers}")
        print("--------------------------------------")

    answer = -1
    if answers:
        answer = min(answers)
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

# Output
print(solution(N4, WEAK4, DIST4))