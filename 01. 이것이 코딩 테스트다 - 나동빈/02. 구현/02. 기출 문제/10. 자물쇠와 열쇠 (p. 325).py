# 10. 자물쇠와 열쇠 (p. 325)
# https://programmers.co.kr/learn/courses/30/lessons/60059

def print_key(key):
    key_row = len(key)
    key_column = len(key[0])
    for i in range(key_row):
        for j in range(key_column):
            print(key[i][j], end=" ")
        print("")
    print("")

def solution(key, lock):
    key_row = len(key)
    key_column = len(key[0])
    print_key(key)

    for _ in range(3):
        new_key = []
        for i in range(key_column):
            temp_key = []
            for j in range(key_row):
                print(f"{i}:{j}, {key[i][j]}")
                temp_key.append(key[i][j])
            new_key.append(temp_key)
        print_key(new_key)

    answer = True
    return answer

# Input
KEY = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
LOCK = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# Output
print(solution(KEY, LOCK))