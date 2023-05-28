# 19. 연산자 끼워 넣기 (p.349)
# https://www.acmicpc.net/problem/14888
import sys

# Input
num_of_numbers = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))


# 주어진 값을 계산하는 함수
def calculate(cal_num1, cal_num2, oper_type):
    if oper_type == 0:
        return cal_num1 + cal_num2
    elif oper_type == 1:
        return cal_num1 - cal_num2
    elif oper_type == 2:
        return cal_num1 * cal_num2
    elif oper_type == 3:
        return int(cal_num1 / cal_num2)


def solution(depth, res):
    # 종료 조건 : 모든 연산자를 사용해서 마지막 연산까지 완료하면 종료한다.
    if depth == num_of_numbers:
        global answer
        if not answer:
            answer = [res, res]
        else:
            answer = [max(answer[0], res), min(answer[1], res)]
        return

    # 루프 조건
    # 1. num1, num2 값 지정
    if depth == 1:
        num1 = numbers[depth - 1]
    else:
        num1 = res
    num2 = numbers[depth]

    global operators
    # 2. 사용 가능한 연산자 리스트(oper_list)를 확인하여 현재 depth(ex. depth 1)에서 할 수 있는 계산을 한다.
    for i in range(4):
        if operators[i]:
            res = calculate(num1, num2, i)
            # 3-1. 사용한 연산자를 전체 연산자 리스트(operators)에서 제외하고 더 깊은 depth(ex. depth 2)로 들어간다.
            # ex. depth 1 -> depth 2-1
            operators[i] -= 1
            solution(depth + 1, res)
            # 3-2. 깊은 depth 계산을 완료하고, 원래의 depth(ex. depth 1)로 되돌아 오면서
            # 다음 차례의 depth(ex. depth 2)를 위해 썼던 연산자를 되돌려놓는다.
            # ex. depth 1 -> depth 2-1 -> depth 3(끝) -> depth 2-2
            operators[i] += 1


answer = []
solution(1, 0)

print(answer[0])
print(answer[1])