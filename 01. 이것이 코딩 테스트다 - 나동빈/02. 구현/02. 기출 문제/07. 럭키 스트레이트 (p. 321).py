# 07. 럭키 스트레이트 (p. 321)
# https://www.acmicpc.net/problem/18406

# Input
score = input()
len_score = len(score)

left_sum = 0
right_sum = 0
for i in range(len_score):
    if i < len_score / 2:
        left_sum += int(score[i])
    else:
        right_sum += int(score[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")