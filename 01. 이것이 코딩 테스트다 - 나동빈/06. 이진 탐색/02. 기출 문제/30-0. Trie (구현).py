class Node:
    def __init__(self, data):
        self.letter = data
        self.children = {}
        self.end_of_word = None


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.end_of_word = string

    def search(self, string):
        current_node = self.root
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.end_of_word == string:
            return True
        else:
            return False


def solution(words):
    answer = []
    trie_words = Trie()
    for word in words:
        trie_words.insert(word)
        print(trie_words.search(word))
    return answer


# Input
words1 = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

# Output
print(solution(words1))