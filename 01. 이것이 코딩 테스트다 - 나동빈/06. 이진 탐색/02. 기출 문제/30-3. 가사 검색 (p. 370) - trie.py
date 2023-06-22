# 30. 가사 검색 (p.370)
# https://school.programmers.co.kr/learn/courses/30/lessons/60060
from collections import deque


class Node:
    def __init__(self, data):
        self.letter = data
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, string):
        current_node = self.root
        deq_next_node = deque()
        for char in string:
            if char != '?':
                if char in current_node.children:
                    current_node = current_node.children[char]
                else:
                    return 0
            else:
                if not deq_next_node:
                    for node in current_node.children.values():
                        deq_next_node.append(node)
                else:
                    for _ in range(len(deq_next_node)):
                        current_node = deq_next_node.popleft()
                        for node in current_node.children.values():
                            deq_next_node.append(node)

        count = 0
        while deq_next_node:
            current_node = deq_next_node.popleft()
            if current_node.is_end_of_word:
                count += 1

        return count


def solution(words, queries):
    answer = []
    trie_words, reversed_trie_words = Trie(), Trie()
    for word in words:
        trie_words.insert(word)
        reversed_trie_words.insert(word[::-1])

    for query in queries:
        if query[0] != '?':
            answer.append(trie_words.search(query))
        else:
            answer.append(reversed_trie_words.search(query[::-1]))
    return answer


# Input
words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries1 = ["fro??", "????o", "fr???", "fro???", "pro?"]

# Output
print(solution(words1, queries1))