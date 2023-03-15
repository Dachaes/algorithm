# 09. 문자열 압축 (p. 323)
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    len_s = int(len(s))
    temp_list = []
    answers = []
    print(f"s의 길이:{len_s}")
    for i in range(1, len_s + 1):                       # i -> 전체 길이(len_s)의 약수만 체크
        temp1 = []
        temp2 = []
        print(f"i: {i} ------")

        cnt = 1
        for j in range(len_s):                      # j -> 리스트 s를 돌리는 변수 (0 ~ len_s)
            if len(temp1) != i:
                temp1.append(s[j])
            else:
                temp2.append((s[j]))

            if len(temp1) == i and len(temp2) == i:
                if temp1 == temp2:
                    cnt += 1
                    print(f"j: {j}, temp1: {temp1}, temp2: {temp2}, cnt: {cnt} / {s}")
                    temp2 = []
                else:
                    if cnt > 1:
                        temp_list.append(str(cnt))
                    temp_list += temp1
                    print(f"j: {j}, temp1: {temp1}, temp2: {temp2}, cnt: {cnt} / {s}")
                    print(f"중간temp_list: {temp_list}")
                    temp1 = temp2
                    cnt = 1
                    temp2 = []

            if j == len_s - 1:
                if cnt > 1:
                    temp_list.append(str(cnt))
                temp_list += temp1
                temp_list += temp2

        print(f"완료temp_list: {temp_list}")
        temp_list = "".join(temp_list)
        answers.append(len(temp_list))
        print(f"answers: {answers}")
        temp_list = []

    answer = min(answers)
    return answer

# Input
S = input()

# Output
print(solution(S))