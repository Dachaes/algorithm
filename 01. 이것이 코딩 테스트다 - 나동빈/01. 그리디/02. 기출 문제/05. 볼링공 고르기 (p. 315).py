# 05. 볼링공 고르기 (p. 315)

# input
N, M = list(map(int, input().split()))
balls = list(map(int, input().split()))

res = 0
for i in range(N):
    ball1 = balls[i]
    for j in range(N):
        ball2 = balls[j]
        if i < j and balls[i] != balls[j]:
            res += 1
print(res)