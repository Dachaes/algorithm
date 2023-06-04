# 22. 블록 이동하기 (p. 355)
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(place, something):
    n, pos1, pos2, state, time = len(place), something[0], something[1], something[2], something[3]
    next_pos_list = []
    for i in range(4):
        next_pos1, next_pos2 = [pos1[0] + dx[i], pos1[1] + dy[i]], [pos2[0] + dx[i], pos2[1] + dy[i]]
        if 0 <= next_pos1[0] < n and 0 <= next_pos1[1] < n and 0 <= next_pos2[0] < n and 0 <= next_pos2[1] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])

    return next_pos_list


def rotate(place, something):
    n, pos1, pos2, state, time = len(place), something[0], something[1], something[2], something[3]
    next_pos_list = []
    if state == 'parallel':
        state = 'vertical'
        # 1. 첫 번째 다리 기준으로 반시계 방향
        next_pos1, next_pos2 = [pos1[0] - 1, pos1[1]], [pos1[0], pos1[1]]
        if 0 <= next_pos1[0] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0]][next_pos1[1] + 1] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])
        # 2. 두 번째 다리 기준으로 반시계 방향
        next_pos1, next_pos2 = [pos2[0], pos2[1]], [pos2[0] + 1, pos2[1]]
        if 0 <= next_pos2[0] < n:
            if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0]][next_pos2[1] - 1] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])
        # 3. 첫 번째 다리 기준으로 시계 방향
        next_pos1, next_pos2 = [pos1[0], pos1[1]], [pos1[0] + 1, pos1[1]]
        if 0 <= next_pos2[0] < n:
            if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0]][next_pos2[1] + 1] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])
        # 4. 두 번째 다리 기준으로 시계 방향
        next_pos1, next_pos2 = [pos2[0] - 1, pos2[1]], [pos2[0], pos2[1]]
        if 0 <= next_pos1[0] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0]][next_pos1[1] - 1] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])
    else:
        state = 'parallel'
        # 1. 첫 번째 다리 기준으로 반시계 방향
        next_pos1, next_pos2 = [pos1[0], pos1[1]], [pos1[0], pos1[1] + 1]
        if 0 <= next_pos2[1] < n:
            if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0] + 1][next_pos2[1]] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])
        # 2. 두 번째 다리 기준으로 반시계 방향
        next_pos1, next_pos2 = [pos2[0], pos2[1] - 1], [pos2[0], pos2[1]]
        if 0 <= next_pos1[1] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0] - 1][next_pos1[1]] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])
        # 3. 첫 번째 다리 기준으로 시계 방향
        next_pos1, next_pos2 = [pos1[0], pos1[1] - 1], [pos1[0], pos1[1]]
        if 0 <= next_pos1[1] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0] + 1][next_pos1[1]] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])
        # 4. 두 번째 다리 기준으로 시계 방향
        next_pos1, next_pos2 = [pos2[0], pos2[1]], [pos2[0], pos2[1] + 1]
        if 0 <= next_pos2[1] < n:
            if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0] - 1][next_pos2[1]] == 0:
                next_pos_list.append([next_pos1, next_pos2, state, time + 1])

    return next_pos_list


def solution(board):
    n = len(board)
    deq_robot = deque([[[0, 0], [0, 1], 'parallel', 0]])
    check_list = [[[0, 0], [0, 1]]]
    while deq_robot:
        robot = deq_robot.popleft()
        move_pos_list = move(board, robot)
        for move_pos in move_pos_list:
            if [move_pos[0], move_pos[1]] not in check_list:
                if move_pos[1] == [n - 1, n - 1]:
                    return move_pos[3]
                else:
                    check_list.append([move_pos[0], move_pos[1]])
                    deq_robot.append(move_pos)

        rotate_pos_list = rotate(board, robot)
        for rotate_pos in rotate_pos_list:
            if [rotate_pos[0], rotate_pos[1]] not in check_list:
                if rotate_pos[1] == [n - 1, n - 1]:
                    return rotate_pos[3]
                else:
                    check_list.append([rotate_pos[0], rotate_pos[1]])
                    deq_robot.append(rotate_pos)


# Input
board0 = [[0, 0, 1, 1],
          [0, 0, 1, 1],
          [0, 0, 1, 1],
          [0, 0, 0, 0]]
# 5
board1 = [[0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0],
          [0, 1, 0, 1, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 0, 0, 0]]
# 7
board2 = [[0, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 0, 0],
          [0, 0, 0, 0]]
# 5
board3 = [[0, 0, 0, 1, 1],
          [0, 0, 1, 1, 0],
          [1, 0, 1, 1, 1],
          [0, 0, 1, 1, 1],
          [0, 0, 0, 0, 0]]
# 8
board4 = [[0, 0, 0, 0, 0, 1],
          [1, 1, 1, 0, 0, 1],
          [1, 0, 0, 1, 0, 0],
          [1, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0]]
# 18
board5 = [[0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0],
          [0, 0, 0, 1, 0, 0],
          [0, 0, 1, 1, 0, 0]]
# 14
board6 = [[0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]
# 7

board7 = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]
# 11

board8 = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
# 21

board9 = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]
# 11

board10 = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]
# 33

# Output
print(solution(board10))