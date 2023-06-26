# 30. 가사 검색 (p. 370)
# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from collections import deque


def filtered_words_by_length(array, filtered_array, length):
    res_array, res_len = [], 0
    if filtered_array[length]:
        return [[], -1]
    else:
        for word in array:
            if length == len(word):
                res_array.append(word)
                res_len += 1
        return [res_array, res_len]


def search_for_words(array, start, end, keyword):
    is_sorted = 0
    if keyword[0] == "?" and keyword[-1] == "?":
        print(f"words(sorted): {array}")
        print(f"===> {len(array)}")
        return len(array)

    start1, start2, end1, end2 = start, start, end, end
    index_first_word, index_last_word = -1, -1
    for i in range(len(keyword)):
        keyword_alphabet = keyword[i]
        if keyword_alphabet != "?":
            if not is_sorted:
                array.sort(key=lambda x: (x[i], x))
                print(f"words(sorted): {array}")
                is_sorted = 1

            while start1 <= end1:
                mid1 = (start1 + end1) // 2
                word1 = array[mid1]
                word1_alphabet = word1[i]
                if keyword_alphabet <= word1_alphabet:
                    if keyword_alphabet == word1_alphabet:
                        index_first_word = mid1
                    end1 = mid1 - 1
                else:
                    start1 = mid1 + 1

            while start2 <= end2:
                mid2 = (start2 + end2) // 2
                word2 = array[mid2]
                word2_alphabet = word2[i]
                if keyword_alphabet < word2_alphabet:
                    end2 = mid2 - 1
                else:
                    if keyword_alphabet == word2_alphabet:
                        index_last_word = mid2
                    start2 = mid2 + 1

            if index_first_word == index_last_word == -1:
                break

    count = 0
    if not (index_first_word == index_last_word == -1):
        deq_words = deque(array[index_first_word:index_last_word + 1])
        for i in range(len(keyword)):
            if keyword[i] != "?":
                for _ in range(len(deq_words)):
                    word = deq_words.popleft()
                    if word[i] == keyword[i]:
                        deq_words.append(word)
        count = len(deq_words)
    print(f"{index_first_word} ~ {index_last_word} ===> {count}")
    return count


def solution(words, queries):
    filtered_words_list = [[] for _ in range(100001)]
    len_filtered_words_list = [-1 for _ in range(100001)]
    answer = []
    print(f"words: {words}")
    print(f"queries: {queries}")
    print(f"------------------------------------")

    for query in queries:
        print(f"-> query: {query}")
        # 1. 찾고자 하는 query와 길이가 같은 word만, filtered_words에 저장한다.
        # -> 이미 분류를 한 word는 filtered_words_list, len_filtered_words_list에 저장한다.
        len_query = len(query)
        temp = filtered_words_by_length(words, filtered_words_list, len_query)
        if temp[0]:
            filtered_words = temp[0]
            len_filtered_words = temp[1]
            filtered_words_list[len_query] = temp[0]
            len_filtered_words_list[len_query] = temp[1]
        else:
            filtered_words = filtered_words_list[len_query]
            len_filtered_words = len_filtered_words_list[len_query]

        # 2. 경우에 따라 sorting 하고, 이진탐색한다.
        answer.append(search_for_words(filtered_words, 0, len_filtered_words - 1, query))
        print(f"------------------------------------")
    return answer


# Input
words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
words2 = ["aa", "ac", "az"]
words3 = ["a", "aaaa", "abaa", "abba", "abbb", "aaba", "aabb"]
queries1_1 = ["fro??", "????o", "fr???", "fro???", "pro?"]
queries1_2 = ["?????", "????", "?????", "?", "??????", "???", "????????"]
queries1_3 = ["????o", "????", "??o", "????t", "kakao", "??oty"]
queries2 = ["a?"]
queries3 = ["?", "a", "b", "???a", "??aa", "??ab", "aa??", "aaa?"]
queries3_1 = ["??ab"]

# Output
print(solution(words1, queries1_1))