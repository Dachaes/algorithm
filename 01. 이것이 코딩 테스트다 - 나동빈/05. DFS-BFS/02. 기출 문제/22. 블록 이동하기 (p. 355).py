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
            else:
                return
        else:
            return
    elif direction == 'down':
        next_pos1, next_pos2 = [something[0][0] + 1, something[0][1]], [something[1][0] + 1, something[1][1]]
        if 0 <= next_pos1[0] < n and 0 <= next_pos2[0] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                return [next_pos1, next_pos2, state, time + 1]
            else:
                return
        else:
            return
    elif direction == 'left':
        next_pos1, next_pos2 = [something[0][0], something[0][1] - 1], [something[1][0], something[1][1] - 1]
        if 0 <= next_pos1[1] < n and 0 <= next_pos2[1] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                return [next_pos1, next_pos2, state, time + 1]
            else:
                return
        else:
            return
    else:
        next_pos1, next_pos2 = [something[0][0], something[0][1] + 1], [something[1][0], something[1][1] + 1]
        if 0 <= next_pos1[1] < n and 0 <= next_pos2[1] < n:
            if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos2[0]][next_pos2[1]] == 0:
                return [next_pos1, next_pos2, state, time + 1]
            else:
                return
        else:
            return


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
                    return
            else:
                return
        else:
            next_pos1, next_pos2 = [something[0][0], something[0][1]], [something[0][0], something[0][1] + 1]
            if 0 <= next_pos2[1] < n:
                if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0] + 1][next_pos2[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]
                else:
                    return
            else:
                return

    else:
        if state == 'parallel':
            next_pos1, next_pos2 = [something[1][0], something[1][1]], [something[1][0] + 1, something[1][1]]
            if 0 <= next_pos2[0] < n:
                if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0]][next_pos2[1] - 1] == 0:
                    state = 'vertical'
                    return [next_pos1, next_pos2, state, time + 1]
                else:
                    return
            else:
                return
        else:
            next_pos1, next_pos2 = [something[1][0], something[1][1] - 1], [something[1][0], something[1][1]]
            if 0 <= next_pos1[1] < n:
                if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[1] - 1][next_pos1[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]
                else:
                    return
            else:
                return


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
                    return
            else:
                return
        else:
            next_pos1, next_pos2 = [something[0][0], something[0][1] - 1], [something[0][0], something[0][1]]
            if 0 <= next_pos1[1] < n:
                if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0] + 1][next_pos1[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]
                else:
                    return
            else:
                return

    else:
        if state == 'parallel':
            next_pos1, next_pos2 = [something[1][0] - 1, something[1][1]], [something[1][0], something[1][1]]
            if 0 <= next_pos1[0] < n:
                if place[next_pos1[0]][next_pos1[1]] == 0 and place[next_pos1[0]][next_pos1[1] - 1] == 0:
                    state = 'vertical'
                    return [next_pos1, next_pos2, state, time + 1]
                else:
                    return
            else:
                return
        else:
            next_pos1, next_pos2 = [something[1][0], something[1][1]], [something[1][0], something[1][1] + 1]
            if 0 <= next_pos2[1] < n:
                if place[next_pos2[0]][next_pos2[1]] == 0 and place[next_pos2[0] - 1][next_pos2[1]] == 0:
                    state = 'parallel'
                    return [next_pos1, next_pos2, state, time + 1]
                else:
                    return
            else:
                return


def solution(board):
    n = len(board)
    deq_robot = deque([[[[0, 0], [0, 1], 'parallel', 0]]])
    check_list = [[[0, 0], [0, 1]]]
    while deq_robot:
        robot_list = deq_robot.popleft()
        temp_next_pos_list = []
        for robot in robot_list:
            next_pos1, next_pos2 = move(board, robot, 'up'), move(board, robot, 'down')
            next_pos3, next_pos4 = move(board, robot, 'left'), move(board, robot, 'right')
            next_pos5, next_pos6 = rotate_counterclockwise(board, robot, 1), rotate_counterclockwise(board, robot, 2)
            next_pos7, next_pos8 = rotate_clockwise(board, robot, 1), rotate_clockwise(board, robot, 2)

            if next_pos1 and [next_pos1[0], next_pos1[1]] not in check_list:
                if next_pos1[1] == [n - 1, n - 1]:
                    return next_pos1[3]
                else:
                    temp_next_pos_list.append(next_pos1)
                    check_list.append([next_pos1[0], next_pos1[1]])
            if next_pos2 and [next_pos2[0], next_pos2[1]] not in check_list:
                if next_pos2[1] == [n - 1, n - 1]:
                    return next_pos2[3]
                else:
                    temp_next_pos_list.append(next_pos2)
                    check_list.append([next_pos2[0], next_pos2[1]])
            if next_pos3 and [next_pos3[0], next_pos3[1]] not in check_list:
                if next_pos3[1] == [n - 1, n - 1]:
                    return next_pos3[3]
                else:
                    temp_next_pos_list.append(next_pos3)
                    check_list.append([next_pos3[0], next_pos3[1]])
            if next_pos4 and [next_pos4[0], next_pos4[1]] not in check_list:
                if next_pos4[1] == [n - 1, n - 1]:
                    return next_pos4[3]
                else:
                    temp_next_pos_list.append(next_pos4)
                    check_list.append([next_pos4[0], next_pos4[1]])
            if next_pos5 and [next_pos5[0], next_pos5[1]] not in check_list:
                if next_pos5[1] == [n - 1, n - 1]:
                    return next_pos5[3]
                else:
                    temp_next_pos_list.append(next_pos5)
                    check_list.append([next_pos5[0], next_pos5[1]])
            if next_pos6 and [next_pos6[0], next_pos6[1]] not in check_list:
                if next_pos6[1] == [n - 1, n - 1]:
                    return next_pos6[3]
                else:
                    temp_next_pos_list.append(next_pos6)
                    check_list.append([next_pos6[0], next_pos6[1]])
            if next_pos7 and [next_pos7[0], next_pos7[1]] not in check_list:
                if next_pos7[1] == [n - 1, n - 1]:
                    return next_pos7[3]
                else:
                    temp_next_pos_list.append(next_pos7)
                    check_list.append([next_pos7[0], next_pos7[1]])
            if next_pos8 and [next_pos8[0], next_pos8[1]] not in check_list:
                if next_pos8[1] == [n - 1, n - 1]:
                    return next_pos8[3]
                else:
                    temp_next_pos_list.append(next_pos8)
                    check_list.append([next_pos8[0], next_pos8[1]])

        if temp_next_pos_list:
            deq_robot.append(temp_next_pos_list)


# Input
board0 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
board1 = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

# Output
print(solution(board0))