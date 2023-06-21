# 30. 가사 검색 (p.370)
# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from bisect import bisect_left, bisect_right


def filtered_words_by_length(array):
    res_array1 = [[] for _ in range(10001)]
    res_array2 = [[] for _ in range(10001)]
    for a in array:
        res_array1[len(a)].append(a)
        res_array2[len(a)].append(a[::-1])
    return [res_array1, res_array2]


def search_for_words(array, first, last):
    first_index = bisect_left(array, first)
    last_index = bisect_right(array, last)

    return last_index - first_index


def solution(words, queries):
    answer = []
    filtered_words = filtered_words_by_length(words)[0]
    reversed_filtered_words = filtered_words_by_length(words)[1]

    for i in range(10001):
        filtered_words[i].sort()
        reversed_filtered_words[i].sort()

    for query in queries:
        if query[0] != '?':
            count = search_for_words(filtered_words[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            count = search_for_words(reversed_filtered_words[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(count)

    return answer


# Input
words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries1 = ["fro??", "????o", "fr???", "fro???", "pro?"]

# Output
print(solution(words1, queries1))