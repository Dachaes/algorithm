# 12. 기둥과 보 설치 (p. 329)
# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    # 전체 좌표의 [기둥, 보]의 정보
    structure = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]          # structure[x좌표][y좌표] = [기둥 유무, 보 유무]
    k = 0
    for frame in build_frame:
        print(f"{k + 1}, build_frame: {frame}")
        x, y = frame[0], frame[1]
        condition = [frame[2], frame[3]]                                        # 0: 기둥, 1: 보 // 0: 삭제, 1: 설치

        # 한 좌표를 기준으로 주변 좌표의 [기둥, 보]의 정보
        surrounding = [[[0, 0] for _ in range(5)] for _ in range(5)]  # surrounding[상대적 x좌표][상대적 y좌표] = [기둥 유무, 보 유무]
        # 좌표값이 범위 밖일 시에 좌표값 조정
        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= x + i <= n and 0 <= y + j <= n:
                    surrounding[i + 2][j + 2] = structure[x + i][y + j]
        print(f"*({x}, {y})를 중심으로 두고, 그 주변 좌표*")
        for i in range(5):
            for j in range(5):
                print(f"{surrounding[i][j]} ", end="")
            print("")

        # 1. 기둥 설치 조건
        # 설치할 기둥이 (1) 바닥 위거나, (2, 3) 보의 한쪽 끝 부분에 위치하거나, (4) 다른 기둥 위에 있을 때
        if condition == [0, 1] and y < n:
            print(f"기둥 설치 조건!!")
            if y == 0 or surrounding[1][2][1] == 1 or surrounding[2][2][1] == 1 or surrounding[2][1][0] == 1:
                print(f"기둥 설치 O")
                structure[x][y][0] = 1
            else:
                print(f"기둥 설치 X")
        # 2. 기둥 삭제 조건
        # (1) 위에 기둥이 있는데 지지해줄 보가 없을 때, (2) 위에 보가 있는데 혼자 남을 때 (3) 왼쪽 위에 보가 있는데 혼자 남을 때는 삭제하지 못한다.
        elif condition == [0, 0]:
            print(f"기둥 삭제 조건!! "
                  f"{(surrounding[2][3][0] == 1 and surrounding[1][3][1] == 0 and surrounding[2][3][1] == 0)}."
                  f"{(surrounding[2][3][1] == 1 and (surrounding[1][3][1] == 0 or surrounding[3][3][1] == 0) and surrounding[3][2][0] == 0)}."
                  f"{(surrounding[1][3][1] == 1 and (surrounding[0][3][1] == 0 or surrounding[2][3][1] == 0) and surrounding[1][2][0] == 0)}")
            if not ((surrounding[2][3][0] == 1 and surrounding[1][3][1] == 0 and surrounding[2][3][1] == 0) or
                    (surrounding[2][3][1] == 1 and (surrounding[1][3][1] == 0 or surrounding[3][3][1] == 0) and surrounding[3][2][0] == 0) or
                    (surrounding[1][3][1] == 1 and (surrounding[0][3][1] == 0 or surrounding[2][3][1] == 0) and surrounding[1][2][0] == 0)):
                print(f"기둥 삭제 O")
                structure[x][y][0] = 0
            else:
                print(f"기둥 삭제 X")
        # 3. 보 설치 조건
        # 설치할 보의 (1) 왼쪽이 기둥 위에 있거나, (2) 오른쪽이 기둥 위에 있거나, (3, 4) 양쪽에 보가 있을 때
        elif condition == [1, 1] and x < n:
            print(f"보 설치 조건!!")
            if surrounding[2][1][0] == 1 or surrounding[3][1][0] == 1 or (surrounding[1][2][1] == 1 and surrounding[3][2][1] == 1):
                # 2-1. 보 설치 조건
                print(f"보 설치 O")
                structure[x][y][1] = 1
            else:
                print(f"보 설치 X")
        # 4. 보 삭제 조건
        # (1) 위에 기둥이 있는데 지지해줄 기둥, 보가 없을 때, (2) 오른쪽 위에 기둥이 있는데 지지해줄 기둥, 보가 없을 때,
        # (3) 왼쪽에 보가 있는데 지지해줄 기둥이 없을 때, (4) 오른쪽에 보가 있는데 지지해줄 기둥이 없을 때는 삭제하지 못한다.
        elif condition == [1, 0]:
            print(f"보 삭제 조건!!")
            if not ((surrounding[2][2][0] == 1 and surrounding[1][2][1] == 0 and surrounding[2][1][0] == 0) or
                    (surrounding[3][2][0] == 1 and surrounding[3][2][1] == 0 and surrounding[3][1][0] == 0) or
                    (surrounding[1][2][1] == 1 and surrounding[1][1][0] == 0 and surrounding[2][1][0] == 0) or
                    (surrounding[3][2][1] == 1 and surrounding[3][1][0] == 0 and surrounding[4][1][0] == 0)):
                print(f"보를 삭제 O")
                structure[x][y][1] = 0
            else:
                print(f"보를 삭제 X")

        print("*현재 좌표 상태*")
        for i in range(n + 1):
            for j in range(n + 1):
                print(f"{structure[i][j]} ", end="")
            print("")

        print("------------------------")
        k += 1
    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            if structure[i][j][0] == 1:
                answer.append([i, j, 0])
            if structure[i][j][1] == 1:
                answer.append([i, j, 1])

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
# [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]

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
# [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]

N3 = 100
BUILD_FRAME3 = [[2, 0, 0, 1],
                [100, 0, 0, 1],
                [100, 1, 1, 1],
                [99, 1, 1, 1],
                [99, 1, 0, 1],
                [99, 0, 0, 1]]
# [[2, 0, 0], [99, 0, 0], [99, 1, 0], [99, 1, 1], [100, 0, 0]]

N4 = 5
BUILD_FRAME4 = [[0, 0, 0, 1],
                [0, 1, 0, 1],
                [0, 2, 0, 1],
                [0, 3, 0, 1],
                [0, 4, 0, 1],
                [0, 5, 0, 1]]
# [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 0]]

N5 = 5
BUILD_FRAME5 = [[0, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 1, 0, 1],
                [0, 1, 1, 1],
                [1, 2, 1, 1],
                [2, 2, 0, 1],
                [2, 3, 1, 1],
                [3, 0, 0, 1],
                [2, 1, 1, 1],
                [3, 1, 0, 1],
                [2, 2, 1, 1],
                [3, 1, 1, 1],
                [4, 1, 0, 1],
                [4, 2, 1, 1],
                [5, 0, 0, 1],
                [5, 2, 0, 1],
                [0, 1, 1, 0],
                [1, 1, 0, 0],
                [1, 2, 1, 0],
                [2, 2, 0, 0],
                [2, 3, 1, 0],
                [3, 0, 0, 0],
                [2, 1, 1, 0],
                [4, 1, 0, 0],
                [5, 0, 0, 0],
                [4, 2, 1, 0],
                [5, 2, 0, 0]]
# [[0, 0, 0],[1, 0, 0],[1, 1, 0],[1, 2, 1],[2, 2, 0], [2, 2, 1],[3, 0, 0],[3, 1, 0],[3, 1, 1],[4, 1, 0],[4, 2, 1]]

# Output
print(solution(N1, BUILD_FRAME1))