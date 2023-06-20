# 30. 가사 검색 (p.370)
# https://school.programmers.co.kr/learn/courses/30/lessons/60060


def search_for_words(array, start, end, keyword):
    is_sorted = 0
    if keyword[0] != "?":
        array.sort()
        print(f"words(sorted): {array}")
        is_sorted = 1

    start1, start2, end1, end2 = start, start, end, end
    mid1, mid2 = (start1 + end1) // 2, (start2 + end2) // 2
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
            start1 = mid1
            end1 = end

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
            start2 = start
            end2 = mid2

            if index_first_word == index_last_word == -1:
                break

    count = 0
    if not (index_first_word == index_last_word == -1):
        count = index_last_word - index_first_word + 1
    elif not is_sorted:
        print(f"words(sorted x): {array}")
        count = end + 1

    print(f"{index_first_word} ~ {index_last_word} ===> {count}")
    return count


def solution(words, queries):
    answer = []
    print(f"words: {words}")
    print(f"queries: {queries}")
    print(f"------------------------------------")

    for query in queries:
        print(f"-> query: {query}")
        # 1. 찾고자 하는 query와 길이가 같은 word만, filtered_words에 저장한다.
        len_query = len(query)
        filtered_words, len_filtered_words = [], 0
        for word in words:
            if len_query == len(word):
                filtered_words.append(word)
                len_filtered_words += 1
        # 2. 경우에 따라 sorting 하고, 이진탐색한다.
        answer.append(search_for_words(filtered_words, 0, len_filtered_words - 1, query))
        print(f"------------------------------------")

    return answer


# Input
words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
words2 = ["aa", "ac", "az"]
queries1_1 = ["fro??", "????o", "fr???", "fro???", "pro?"]
queries1_2 = ['?????', '????', '?????', '??????', '???', '????????']
queries1_3 = ['fro?', 'f?', '?r', '????t', '?????']
queries2 = ["a?"]

# Output
print(solution(words2, queries2))