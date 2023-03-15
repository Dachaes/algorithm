# 10. 자물쇠와 열쇠 (p. 325)
# https://programmers.co.kr/learn/courses/30/lessons/60059

def print_key(key):
    row = len(key)
    column = len(key[0])
    for i in range(row):
        for j in range(column):
            print(key[i][j], end=" ")
        print("")
    print("")

def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    print_key(key)

    def rotate_90(matrix):
        new_matrix = []
        for i in range(len_key):
            temp = []
            for j in range(len_key - 1, -1, -1):
                temp.append(matrix[j][i])
            new_matrix.append(temp)
        return new_matrix

    for _ in range(3):
        new_key = []
        for i in range(len_key - 1):



        key = rotate_90(key)
        print_key(key)


    answer = True
    return answer

# Input
KEY = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
LOCK = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# Output
print(solution(KEY, LOCK))