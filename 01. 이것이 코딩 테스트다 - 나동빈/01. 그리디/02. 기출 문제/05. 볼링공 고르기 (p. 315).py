# 05. 볼링공 고르기 (p. 315)

# Input
N, M = list(map(int, input().split()))
balls = list(map(int, input().split()))

res = 0
for i in range(N):
    for j in range(N):
        if i < j and balls[i] != balls[j]:
            res += 1
print(res)