# 25. 실패율 (p. 361)
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    len_stages = len(stages)
    users = []

    for stage in range(1, N + 1):
        cnt = stages.count(stage)
        if cnt == 0:
            users.append([stage, 0])
        else:
            users.append([stage, cnt / len_stages])
        len_stages -= cnt

    users.sort(key=lambda x: (-x[1], x[0]))

    answer = []
    for user in users:
        answer.append(user[0])

    return users

# Input
N1 = 5
STAGES1 = [2, 1, 2, 6, 2, 4, 3, 3]
# [3, 4, 2, 1, 5]

N2 = 4
STAGES2 = [4, 4, 4, 4, 4]
# [4, 1, 2, 3]

N3 = 2
STAGES3 = [1, 1]
# [1, 2]

# Output
print(solution(N3, STAGES3))