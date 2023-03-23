# 14. 외벽 점검 (p. 335)
# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations

def solution(n, weak, friends):
    len_weak = len(weak)
    num_friends = len(friends)

    extended_weak = []
    for i in range(2 * len_weak):
        if i < len_weak:
            extended_weak.append(weak[i])
        else:
            extended_weak.append(weak[i - len_weak] + n)

    print(f"** n: {n}개의 원형 레스토랑")
    print(f"** 취약점 리스트(weak): {weak}")
    print(f"** 취약점 리스트-확장(extended_weak): {extended_weak}")

    friends_groups = list(permutations(friends))
    print(f"** 친구 리스트(friends): {friends}")
    print(f"** 친구 리스트-순열(friends_groups): {friends_groups}")

    # 1. 시작 지점을 처음부터 전체 레스토랑의 크기만큼 전부 체크한다. (0 ~ n-1)
    answers = []
    for start in range(len_weak):
        print("----------------------------------")
        print(f"==> {weak[start]}부터 시작!")
        # 2. 친구가 출발 지점부터 어디까지 체크할 수 있는지 확인한다. (pos)
        for friends_group in friends_groups:
            count = 1
            pos1 = extended_weak[start]
            pos2 = pos1 + friends_group[count - 1]
            for index in range(start, start + len_weak):
                print(f"-> count: {count}명 째 체크 중~ [pos: {pos1} ~ {pos2}]")
                print(f"친구 리스트(friends_group): {friends_group}")
                print(f"-> index: {index} => {extended_weak[index]}")
                print(f"확장한 취약점 리스트(extended_weak): {extended_weak}")
                if pos2 < extended_weak[index]:
                    count += 1
                    if num_friends < count:
                        break
                    pos2 = extended_weak[index] + friends_group[count - 1]
                print("----------------------------------")
            answers.append(count)

    answer = min(answers)
    if answer == num_friends + 1:
        answer = -1
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
print(solution(N1, WEAK1, DIST1))