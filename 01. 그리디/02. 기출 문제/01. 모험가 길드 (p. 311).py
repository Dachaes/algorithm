# 01. 모험가 길드 (p. 311)

# input
N = int(input())
people = list(map(int, input().split()))

num_of_people = []                          # 각 공포도 별, 사람 수를 리스트로 저장
for i in range(1, N + 1):
    num_of_people.append(people.count(i))

temp = 0
num_of_group = 0
for i in range(1, N + 1):
    temp += num_of_people[i - 1]
    if temp >= i:
        num_of_group += temp // i
        temp = temp % i

print(num_of_group)