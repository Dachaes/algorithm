# 19. 연산자 끼워 넣기 (p.349)
# https://www.acmicpc.net/problem/14888
import sys
from copy import deepcopy
from collections import deque

# Input
num_of_numbers = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

deq_numbers = deque(numbers)


# 연산자 리스트(operators_list)에서 연산자 하나를 pop하는 함수
def pop_operator(operators_list):
    for i in range(4):
        if operators_list[i] != 0:
            operator_type = i
            operators_list[i] -= 1
            break
    return operator_type


# 주어진 값을 계산하는 함수
def calculate(cal_num1, cal_num2, type):
    if type == 0:
        return cal_num1 + cal_num2
    elif type == 1:
        return cal_num1 - cal_num2
    elif type == 2:
        return cal_num1 * cal_num2
    else:
        return cal_num1 // cal_num2


def solution(count, res, def_numbers, def_operators):
    print(f"--------------------------------------------------")
    print(f"기본 : numbers: {def_numbers}, operators: {def_operators}")
    # 종료 조건 : 모든 연산자를 사용해서 마지막 연산까지 완료하면 종료한다.
    if count == num_of_numbers - 1:
        global answer
        if not answer:
            answer = [res, res]
        else:
            answer = [max(answer[0], res), min(answer[1], res)]
        print(f"  종료")
        print(f"--------------------------------------------------")
        return

    # 루프 조건
    elif count == 0:
        new_numbers = deepcopy(def_numbers)
        num1, num2 = new_numbers.popleft(), new_numbers.popleft()
    else:
        new_numbers = deepcopy(def_numbers)
        num1, num2 = res, new_numbers.popleft()

    new_operators1 = deepcopy(def_operators)
    for _ in range(count, num_of_numbers - 1):
        new_operators2 = deepcopy(def_operators)
        operators_type = pop_operator(new_operators1)
        new_operators2[operators_type] -= 1
        print(f"{count}--- num: {num1}, {num2}, operators_type: {operators_type}")
        res = calculate(num1, num2, operators_type)
        print(f"  res: {res}")
        print(f"--------------------------------------------------")
        solution(count + 1, res, new_numbers, new_operators2)



answer = []
solution(0, 0, deq_numbers, operators)

print(answer[0])
print(answer[1])