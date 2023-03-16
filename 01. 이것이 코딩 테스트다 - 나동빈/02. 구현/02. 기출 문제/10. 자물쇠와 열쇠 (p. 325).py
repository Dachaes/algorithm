# 10. 자물쇠와 열쇠 (p. 325)
# https://programmers.co.kr/learn/courses/30/lessons/60059

def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    len_special_key = len_lock + (len_key - 1) * 2

    # 함수: key를 확장한 크기만큼의 special_key를 만들고, (x, y)위치 부터 key의 값으로 초기화
    def initialize_special_key(original_key, x, y):
        new_key = [[0] * len_special_key for _ in range(len_special_key)]
        for i in range(len_key):
            for j in range(len_key):
                new_key[i + x][j + y] = original_key[i][j]
        return new_key

    # 함수: special_key의 맨 중앙 부분이 lock과 같은지 확인
    # key와 lock은 홈(0)과 돌기(1)부분이 맞아야 하므로, 비교할 때에는 key의 값을 반전시켜야 함
    def compare_key_and_lock(original_key):
        new_key = [[1] * len_lock for _ in range(len_lock)]
        for i in range(len_lock):
            for j in range(len_lock):
                new_key[i][j] = (original_key[i + (len_key - 1)][j + (len_key - 1)]) ^ 1
        if new_key == lock:
            return True
        return False

    # 함수: key를 회전
    def rotate_90(original_key):
        new_key = list(map(list, zip(*original_key[::-1])))
        return new_key

    # 1. 원본 key를 확장한 크기만큼의 special_key를 생성한다.
    special_key = []
    for _ in range(4):
        # 2. special_key의 값을 움직여보고,
        for i in range(len_lock + len_key - 1):
            for j in range(len_lock + len_key - 1):
                special_key = initialize_special_key(key, i, j)
                # 3. 움직일 때마다 자물쇠(lock)에 맞는 열쇠(special_key의 중앙값)인지 확인한다.
                if compare_key_and_lock(special_key):
                    return True
        # 4. 원본 key를 90도 회전한다.
        key = rotate_90(key)

    return False

# Input
KEY1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
LOCK1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
KEY2 = [[0, 1], [1, 0]]
LOCK2 = [[1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

# Output
print(solution(KEY1, LOCK1))