# 02. 성적이 낮은 순서로 학생 출력하기 (p. 180)

# Input
num = int(input())
students = []
for _ in range(num):
    data = input().split()
    students.append([data[0], int(data[1])])

def score(array):
    return array[1]

students.sort(key=score)

for i in range(num):
    print(students[i][0], end=" ")