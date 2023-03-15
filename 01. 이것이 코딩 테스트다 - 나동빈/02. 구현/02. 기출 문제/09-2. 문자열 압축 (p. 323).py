# 09. 문자열 압축 (p. 323)
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    len_s = int(len(s))
    temp_list = []
    answers = [len_s]
    for i in range(1, (len_s // 2) + 1):       # i -> 한 묶음 안의 문자 개수
        temp1 = []
        temp2 = []
        cnt = 1
        for j in range(len_s):      # j -> 리스트 s를 돌리는 변수 (0 ~ len_s)
            # 1. temp1, temp2에 i만큼의 비교할 문자를 저장한다.
            if len(temp1) != i:
                temp1.append(s[j])
            else:
                temp2.append((s[j]))
            # 2. 원하는 개수만큼 temp1, temp2에 문자가 쌓였다면
            # 서로 비교해주고 temp_list에 임시로 저장한다. (이를 끝까지 반복한다.)
            if len(temp1) == i and len(temp2) == i:
                # 2-1. temp1과 temp2가 같으면 count를 올린다.
                if temp1 == temp2:
                    cnt += 1
                # 2-2. temp1과 temp2가 다르면 cnt와 temp1을 temp_list에 추가하고, 기존 temp2를 temp1로 옮긴다.
                else:
                    if cnt > 1:
                        temp_list.append(str(cnt))
                    temp_list += temp1
                    temp1 = temp2
                    cnt = 1
                # 다음에 비교할 문자를 위해 temp2를 비운다.
                temp2 = []

            # 3. j의 for 문의 마지막 차례가 오면, 마지막 temp2를 저장하지 못하므로 temp_list에 이를 추가로 저장한다.
            # (앞서 temp1과 temp2가 계속 같았어서 마지막에 temp_list에 추가되지 못한 경우도 마찬가지)
            if j == len_s - 1:
                if cnt > 1:
                    temp_list.append(str(cnt))
                temp_list += temp1
                temp_list += temp2

        # 4. temp_list의 문자의 개수를 answers에 추가하고, 다음 i를 위해 temp_list를 비운다.
        temp_list = "".join(temp_list)
        answers.append(len(temp_list))
        temp_list = []

    #5. 가장 효율적인(가장 최소의) 문자열 압축의 문자의 개수를 찾는다.
    answer = min(answers)
    return answer

# Input
S = input()

# Output
print(solution(S))