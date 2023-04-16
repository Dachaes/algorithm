# 36. 편집 거리 (p. 382)

# Input
word_A, word_B = input(), input()
len_A, len_B = len(word_A), len(word_B)

edit_distance = [[0] * (len_B + 1) for _ in range(len_A + 1)]
for i in range(len_A + 1):
    for j in range(len_B + 1):
        if i == 0:
            edit_distance[0][j] = j
        elif j == 0:
            edit_distance[i][0] = i
        elif word_A[i - 1] == word_B[j - 1]:
            edit_distance[i][j] = edit_distance[i - 1][j - 1]
        else:
            edit_distance[i][j] = min(edit_distance[i - 1][j - 1], edit_distance[i - 1][j], edit_distance[i][j - 1]) + 1

print(edit_distance[-1][-1])