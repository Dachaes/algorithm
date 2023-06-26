# 30. 가사 검색 (p. 370)
# https://school.programmers.co.kr/learn/courses/30/lessons/60060
class Node:
    def __init__(self, data):
        self.letter = data
        self.count = 0
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node(None)
        self.count = 0
    def insert(self, string):
        current_node = self.root
        self.count += 1

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.count += 1
        current_node.is_end_of_word = True

    def search(self, string):
        current_node = self.root
        for char in string:
            if char != '?':
                if char in current_node.children:
                    current_node = current_node.children[char]
                else:
                    return 0
            else:
                break

        return current_node.count


def solution(words, queries):
    answer = []
    trie_words, reversed_trie_words = {}, {}
    for word in words:
        if len(word) not in trie_words:
            trie_words[len(word)] = Trie()
            reversed_trie_words[len(word)] = Trie()

        trie_words[len(word)].insert(word)
        reversed_trie_words[len(word)].insert(word[::-1])

    for query in queries:
        if len(query) not in trie_words:
            answer.append(0)
        elif len(query) == query.count('?'):
            answer.append(trie_words[len(query)].count)
        elif query[0] != '?':
            answer.append(trie_words[len(query)].search(query))
        else:
            answer.append(reversed_trie_words[len(query)].search(query[::-1]))
    return answer


# Input
words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries1 = ["fro??", "????o", "fr???", "fro???", "pro?"]

# Output
print(solution(words1, queries1))