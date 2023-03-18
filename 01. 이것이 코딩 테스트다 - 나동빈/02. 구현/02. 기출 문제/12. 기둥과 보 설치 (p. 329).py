# 12. 기둥과 보 설치 (p. 329)
# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            answer.append([i, j, 3])
    for i in range(len(build_frame)):
        location = [build_frame[1], build_frame[0]]
        condition = (build_frame[2], build_frame[3])
        # 1. 기둥 설치 조건
        if condition == (0, 1):
            if location[]
        # 2. 보 설치 조건
        elif condition == (1, 1):
        # 3. 기둥 삭제 조건
        elif condition == (1, 0):
        # 4. 보 삭제 조건
        else:

    return answer

# Input
N1 = 5
BUILD_FRAME1 = [[1, 0, 0, 1],
                [1, 1, 1, 1],
                [2, 1, 0, 1],
                [2, 2, 1, 1],
                [5, 0, 0, 1],
                [5, 1, 0, 1],
                [4, 2, 1, 1],
                [3, 2, 1, 1]]
N2 = 5
BUILD_FRAME2 = [[0, 0, 0, 1],
                [2, 0, 0, 1],
                [4, 0, 0, 1],
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [2, 1, 1, 1],
                [3, 1, 1, 1],
                [2, 0, 0, 0],
                [1, 1, 1, 0],
                [2, 2, 0, 1]]
# Output
print(solution(N1, BUILD_FRAME1))