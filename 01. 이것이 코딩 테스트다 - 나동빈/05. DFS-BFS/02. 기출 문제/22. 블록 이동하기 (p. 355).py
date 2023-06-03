# 22. 블록 이동하기 (p. 355)
# https://programmers.co.kr/learn/courses/30/lessons/60063
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(place, something, time, direction):
    n = len(place)
    if direction == 'up':
        next_pos_1, next_pos_2 = [something[0][0] - 1, something[0][1]], [something[1][0] - 1, something[1][1]]
        if 1 <= next_pos_1[0] <= n and 1 <= next_pos_2[0] <= n:
            if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_2[0]][next_pos_2[1]] == 0:
                return [[next_pos_1], [next_pos_2], something[2], time + 1]
        else:
            return
    elif direction == 'down':
        next_pos_1, next_pos_2 = [something[0][0] + 1, something[0][1]], [something[1][0] + 1, something[1][1]]
        if 1 <= next_pos_1[0] <= n and 1 <= next_pos_2[0] <= n:
            if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_2[0]][next_pos_2[1]] == 0:
                return [[next_pos_1], [next_pos_2], something[2], time + 1]
        else:
            return
    elif direction == 'left':
        next_pos_1, next_pos_2 = [something[0][0], something[0][1] - 1], [something[1][0], something[1][1] - 1]
        if 1 <= next_pos_1[1] <= n and 1 <= next_pos_2[1] <= n:
            if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_2[0]][next_pos_2[1]] == 0:
                return [[next_pos_1], [next_pos_2], something[2], time + 1]
        else:
            return
    else:
        next_pos_1, next_pos_2 = [something[0][0], something[0][1] + 1], [something[1][0], something[1][1] + 1]
        if 1 <= next_pos_1[1] <= n and 1 <= next_pos_2[1] <= n:
            if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_2[0]][next_pos_2[1]] == 0:
                return [[next_pos_1], [next_pos_2], something[2], time + 1]
        else:
            return


# 로봇의 다리(leg)를 축으로 반시계 방향으로 돌리는 함수
def rotate_counterclockwise(place, something, time, leg):
    n, state = len(place), something[2]
    if leg == 1:
        if state == 'parallel':
            next_pos_1, next_pos_2 = [something[0][0] - 1, something[0][1]], [something[0][0], something[0][1]]
            if 1 <= next_pos_1[0] <= n:
                if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_1[0]][next_pos_1[1] + 1] == 0:
                    state = 'vertical'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return
        else:
            next_pos_1, next_pos_2 = [something[0][0], something[0][1]], [something[0][0], something[0][1] + 1]
            if 1 <= next_pos_2[1] <= n:
                if place[next_pos_2[0]][next_pos_2[1]] == 0 and place[next_pos_2[0] + 1][next_pos_2[1]] == 0:
                    state = 'parallel'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return

    else:
        if state == 'parallel':
            next_pos_1, next_pos_2 = [something[1][0], something[1][1]], [something[1][0] + 1, something[1][1]]
            if 1 <= next_pos_2[0] <= n:
                if place[next_pos_2[0]][next_pos_2[1]] == 0 and place[next_pos_1[0]][next_pos_1[1] - 1] == 0:
                    state = 'vertical'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return
        else:
            next_pos_1, next_pos_2 = [something[1][0], something[1][1] - 1], [something[1][0], something[1][1]]
            if 1 <= next_pos_1[1] <= n:
                if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_1[0] - 1][next_pos_1[1]] == 0:
                    state = 'parallel'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return


# 로봇의 다리(leg)를 축으로 시계 방향으로 돌리는 함수
def rotate_clockwise(place, something, time, leg):
    n, state = len(place), something[2]
    if leg == 1:
        if state == 'parallel':
            next_pos_1, next_pos_2 = [something[0][0], something[0][1]], [something[0][0] + 1, something[0][1]]
            if 1 <= next_pos_2[0] <= n:
                if place[next_pos_2[0]][next_pos_2[1]] == 0 and place[next_pos_2[0]][next_pos_2[1] + 1] == 0:
                    state = 'vertical'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return
        else:
            next_pos_1, next_pos_2 = [something[0][0], something[0][1] - 1], [something[0][0], something[0][1]]
            if 1 <= next_pos_1[1] <= n:
                if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_1[0] + 1][next_pos_1[1]] == 0:
                    state = 'parallel'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return

    else:
        if state == 'parallel':
            next_pos_1, next_pos_2 = [something[1][0] - 1, something[1][1]], [something[1][0], something[1][1]]
            if 1 <= next_pos_1[0] <= n:
                if place[next_pos_1[0]][next_pos_1[1]] == 0 and place[next_pos_1[0]][next_pos_1[1] - 1] == 0:
                    state = 'vertical'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return
        else:
            next_pos_1, next_pos_2 = [something[1][0], something[1][1]], [something[1][0], something[1][1] + 1]
            if 1 <= next_pos_2[1] <= n:
                if place[next_pos_2[0]][next_pos_2[1]] == 0 and place[next_pos_2[0] - 1][next_pos_2[1]] == 0:
                    state = 'parallel'
                    return [[next_pos_1], [next_pos_2], state, time + 1]
            else:
                return


def solution(board):
    n = max(board)
    deq_robot = deque([[[1, 1], [1, 2], 'parallel', 0]])
    check_list = [[[1, 1], [1, 2]]]
    while deq_robot:
        robot_list = deq_robot.pop()
        for robot in robot_list:

# Input
board0 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
board1 = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

# Output
print(solution(board0))