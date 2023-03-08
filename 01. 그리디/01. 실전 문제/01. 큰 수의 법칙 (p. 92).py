# 01. 큰 수의 법칙 (p. 92)

# input
N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

sorted_num_list = sorted(num_list)
max1_value = sorted_num_list[-1]
max2_value = sorted_num_list[-2]
res = 0

if max1_value == max2_value:
    res = M * max1_value
else:
    k = K
    for i in range(M):
        if k != 0:
            res += max1_value
            k -= 1
        else:
            res += max2_value
            k = K

print(res)