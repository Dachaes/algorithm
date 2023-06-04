# 22. 블록 이동하기 (p. 355)
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque


def move(place, something, direction):
    n, state, time = len(place), something[2], something[3]
    if direction == 'up':
        next_pos1, next_pos2 = [something[0][0] - 1, something[0][1]], [something[1][0] - 1, something[1][1]]
        if 0 <= next_pos1[0] < n and 0 <= next_pos2[0] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                return [next_pos1, next_pos2, state, time + 1]
    elif direction == 'down':
        next_pos1, next_pos2 = [something[0][0] + 1, something[0][1]], [something[1][0] + 1, something[1][1]]
        if 0 <= next_pos1[0] < n and 0 <= next_pos2[0] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                return [next_pos1, next_pos2, state, time + 1]
    elif direction == 'left':
        next_pos1, next_pos2 = [something[0][0], something[0][1] - 1], [something[1][0], something[1][1] - 1]
        if 0 <= next_pos1[1] < n and 0 <= next_pos2[1] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                return [next_pos1, next_pos2, state, time + 1]
    else:
        next_pos1, next_pos2 = [something[0][0], something[0][1] + 1], [something[1][0], something[1][1] + 1]
        if 0 <= next_pos1[1] < n and 0 <= next_pos2[1] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                return [next_pos1, next_pos2, state, time + 1]


# 로봇의 다리(leg)를 축으로 반시계 방향으로 돌리는 함수
def rotate_counterclockwise(place, something, leg):
    n, state, time = len(place), something[2], something[3]
    if leg == 1:
        if state == 'parallel':
            next_pos1, next_pos2 = [something[0][0] - 1, something[0][1]], [something[0][0], something[0][1]]
            if 0 <= next_pos1[0] < n:
                if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0]][next_pos1[1] + 1] == 0:
                    state = 'vertical'
                    return [next_pos1, next_pos2, state, time + 1]
        else:
            next_pos1, next_pos2 = [something[0][0], something[0][1]], [something[0][0], something[0][1] + 1]
            if 0 <= next_pos2[1] < n:
                if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0] + 1][next_pos2[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]
    else:
        if state == 'parallel':
            next_pos1, next_pos2 = [something[1][0], something[1][1]], [something[1][0] + 1, something[1][1]]
            if 0 <= next_pos2[0] < n:
                if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0]][next_pos2[1] - 1] == 0:
                    state = 'vertical'
                    return [next_pos1, next_pos2, state, time + 1]
        else:
            next_pos1, next_pos2 = [something[1][0], something[1][1] - 1], [something[1][0], something[1][1]]
            if 0 <= next_pos1[1] < n:
                if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0] - 1][next_pos1[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]


# 로봇의 다리(leg)를 축으로 시계 방향으로 돌리는 함수
def rotate_clockwise(place, something, leg):
    n, state, time = len(place), something[2], something[3]
    if leg == 1:
        if state == 'parallel':
            next_pos1, next_pos2 = [something[0][0], something[0][1]], [something[0][0] + 1, something[0][1]]
            if 0 <= next_pos2[0] < n:
                if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0]][next_pos2[1] + 1] == 0:
                    state = 'vertical'
                    return [next_pos1, next_pos2, state, time + 1]
        else:
            next_pos1, next_pos2 = [something[0][0], something[0][1] - 1], [something[0][0], something[0][1]]
            if 0 <= next_pos1[1] < n:
                if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0] + 1][next_pos1[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]
    else:
        if state == 'parallel':
            next_pos1, next_pos2 = [something[1][0] - 1, something[1][1]], [something[1][0], something[1][1]]
            if 0 <= next_pos1[0] < n:
                if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0]][next_pos1[1] - 1] == 0:
                    state = 'vertical'
                    return [next_pos1, next_pos2, state, time + 1]
        else:
            next_pos1, next_pos2 = [something[1][0], something[1][1]], [something[1][0], something[1][1] + 1]
            if 0 <= next_pos2[1] < n:
                if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0] - 1][next_pos2[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]


def solution(board):
    n = len(board)
    deq_robot = deque([[[0, 0], [0, 1], 'parallel', 0]])
    check_list = [[[0, 0], [0, 1]]]
    while deq_robot:
        print(f"--> deq_robot: {deq_robot}")
        robot = deq_robot.popleft()
        print(f"--> robot: {robot}")
        next_pos1, next_pos2 = move(board, robot, 'up'), move(board, robot, 'down')
        next_pos3, next_pos4 = move(board, robot, 'left'), move(board, robot, 'right')
        next_pos5, next_pos6 = rotate_counterclockwise(board, robot, 1), rotate_counterclockwise(board, robot, 2)
        next_pos7, next_pos8 = rotate_clockwise(board, robot, 1), rotate_clockwise(board, robot, 2)
        print(f"상: {next_pos1}")
        print(f"하: {next_pos2}")
        print(f"좌: {next_pos3}")
        print(f"우: {next_pos4}")
        print(f"반시계(1): {next_pos5}")
        print(f"반시계(2): {next_pos6}")
        print(f"시계(1): {next_pos7}")
        print(f"시계(2): {next_pos8}")

        if next_pos1 and [next_pos1[0], next_pos1[1]] not in check_list:
            if next_pos1[1] == [n - 1, n - 1]:
                return next_pos1[3]
            else:
                check_list.append([next_pos1[0], next_pos1[1]])
                deq_robot.append(next_pos1)
        if next_pos2 and [next_pos2[0], next_pos2[1]] not in check_list:
            if next_pos2[1] == [n - 1, n - 1]:
                return next_pos2[3]
            else:
                check_list.append([next_pos2[0], next_pos2[1]])
                deq_robot.append(next_pos2)
        if next_pos3 and [next_pos3[0], next_pos3[1]] not in check_list:
            if next_pos3[1] == [n - 1, n - 1]:
                return next_pos3[3]
            else:
                check_list.append([next_pos3[0], next_pos3[1]])
                deq_robot.append(next_pos3)
        if next_pos4 and [next_pos4[0], next_pos4[1]] not in check_list:
            if next_pos4[1] == [n - 1, n - 1]:
                return next_pos4[3]
            else:
                check_list.append([next_pos4[0], next_pos4[1]])
                deq_robot.append(next_pos4)
        if next_pos5 and [next_pos5[0], next_pos5[1]] not in check_list:
            if next_pos5[1] == [n - 1, n - 1]:
                return next_pos5[3]
            else:
                check_list.append([next_pos5[0], next_pos5[1]])
                deq_robot.append(next_pos5)
        if next_pos6 and [next_pos6[0], next_pos6[1]] not in check_list:
            if next_pos6[1] == [n - 1, n - 1]:
                return next_pos6[3]
            else:
                check_list.append([next_pos6[0], next_pos6[1]])
                deq_robot.append(next_pos6)
        if next_pos7 and [next_pos7[0], next_pos7[1]] not in check_list:
            if next_pos7[1] == [n - 1, n - 1]:
                return next_pos7[3]
            else:
                check_list.append([next_pos7[0], next_pos7[1]])
                deq_robot.append(next_pos7)
        if next_pos8 and [next_pos8[0], next_pos8[1]] not in check_list:
            if next_pos8[1] == [n - 1, n - 1]:
                return next_pos8[3]
            else:
                check_list.append([next_pos8[0], next_pos8[1]])
                deq_robot.append(next_pos8)
        print(f"------------------------------")


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