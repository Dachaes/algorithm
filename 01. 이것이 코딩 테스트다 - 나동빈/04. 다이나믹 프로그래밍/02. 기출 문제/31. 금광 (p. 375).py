# 31. 금광 (p. 375)

# Input
num_testcase = int(input())

while num_testcase != 0:
    # Input
    row, column = map(int, input().split())
    gold_input = list(map(int, input().split()))
    mine = []
    for i in range(0, len(gold_input), column):
        mine.append(gold_input[i:i + column])

    sum_gold = [[0] * column for _ in range(row)]
    answers = []
    for j in range(column):
        for i in range(row):
            if j == 0:
                sum_gold[i][j] = mine[i][j]
            else:
                left_up = [i - 1, j - 1]
                left_mid = [i, j - 1]
                left_right = [i + 1, j - 1]
                left = []
                if 0 <= left_up[0] < row:
                    left.append(sum_gold[left_up[0]][left_up[1]])
                if 0 <= left_mid[0] < row:
                    left.append(sum_gold[left_mid[0]][left_mid[1]])
                if 0 <= left_right[0] < row:
                    left.append(sum_gold[left_right[0]][left_right[1]])
                sum_gold[i][j] = mine[i][j] + max(left)

            if j == column - 1:
                answers.append(sum_gold[i][j])

    print(max(answers))
    num_testcase -= 1