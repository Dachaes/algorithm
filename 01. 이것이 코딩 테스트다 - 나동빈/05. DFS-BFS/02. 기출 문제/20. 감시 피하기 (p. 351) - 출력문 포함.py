# 20. 감시 피하기 (p. 351)
# https://www.acmicpc.net/problem/18428
import sys
from itertools import combinations

# Input
n = int(input())
corridor = []
for _ in range(n):
    corridor.append(list(sys.stdin.readline().replace(' ', '').strip('\n')))

students = []
teachers = []
blank_space = []
for i in range(n):
    for j in range(n):
        if corridor[i][j] == 'S':
            students.append((i, j))
        elif corridor[i][j] == 'T':
            teachers.append((i, j))
        else:
            blank_space.append((i, j))
walls = list(combinations(blank_space, 3))


# 선생님들의 위치를 가지고 있는 리스트(teachers)를 불러와서 감시하는 곳에 학생이 있는지 확인하는 함수
# 어떤 선생님이든 한 명이라도 학생을 발견하면 TRUE를 반환한다.
def supervise(people):
    for person in people:
        print(f"teacher: {person}")
        person_x, person_y = person[0], person[1]
        check_x, check_y = person_x, person_y
        while check_x > 0:
            check_x -= 1
            print(f"1. ({check_x}, {check_y}) 확인 중~")
            if (check_x, check_y) in wall:
                print(f" 1. 벽이 있습니다!")
                break
            elif (check_x, check_y) in students:
                print(f" 1. 학생이 있습니다.")
                return True
        check_x = person_x
        while check_x < n - 1:
            check_x += 1
            print(f"2. ({check_x}, {check_y}) 확인 중~")
            if (check_x, check_y) in wall:
                print(f" 2. 벽이 있습니다!")
                break
            elif (check_x, check_y) in students:
                print(f" 2. 학생이 있습니다.")
                return True
        check_x = person_x
        while check_y > 0:
            check_y -= 1
            print(f"3. ({check_x}, {check_y}) 확인 중~")
            if (check_x, check_y) in wall:
                print(f" 3. 벽이 있습니다!")
                break
            elif (check_x, check_y) in students:
                print(f" 3. 학생이 있습니다.")
                return True
        check_y = person_y
        while check_y < n - 1:
            check_y += 1
            print(f"4. ({check_x}, {check_y}) 확인 중~")
            if (check_x, check_y) in wall:
                print(f" 4. 벽이 있습니다!")
                break
            elif (check_x, check_y) in students:
                print(f" 4. 학생이 있습니다.")
                return True
    return False


ans = 'NO'
# 모든 경우의 벽을 세우고 매번 복도를 감시했을 때, 선생님들의 시선 하에 단 한 명의 학생도 없던 적이 있으면 ans에 'YES'를 할당한다.
for wall in walls:
    print(f"wall: {wall}")
    print(f"반환값: {supervise(teachers)}")
    # if not supervise(teachers):
    #     ans = 'YES'
    #     break
    print(f"--------------------------------------")
print(ans)