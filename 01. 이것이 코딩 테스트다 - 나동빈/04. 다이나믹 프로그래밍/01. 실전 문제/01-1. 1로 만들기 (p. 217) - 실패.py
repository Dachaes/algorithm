# 01. 1로 만들기 (p. 217)
# 해당 코드는 X가 n제곱수일 때, 연산의 최솟값을 구하지 못한다.

# Input
X = int(input())

cnt = 0
num = 1
while num != X:
    temps = [num * 5, num * 3, num * 2, num + 1]
    max_temp = 0
    for temp in temps:
        if max_temp < temp <= X:
            max_temp = temp

    num = max_temp
    cnt += 1

print(cnt)