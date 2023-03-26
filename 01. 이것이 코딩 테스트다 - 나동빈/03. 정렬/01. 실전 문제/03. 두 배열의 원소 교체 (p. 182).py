# 03. 두 배열의 원소 교체 (p. 182)

# Input
N, K = map(int, input().split())
num1_list = list(map(int, input().split()))
num2_list = list(map(int, input().split()))

num1_list.sort()
num2_list.sort(reverse=True)

for index in range(N):
    num1 = num1_list[index]
    num2 = num2_list[index]
    if K == 0:
        break
    elif num1 < num2:
        num1_list[index] = num2_list[index]
        K -= 1
    else:
        break

res = sum(num1_list)
print(res)