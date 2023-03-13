# 08. 문자열 재정렬 (p. 322)

# Input
words = input()

alphabet_words = []
number_words = []
sorted_words = []
for i in range(len(words)):
    word = words[i]
    if 48 <= ord(word) <= 57:           # x.isdigit(), x.isdecimal(), x.isnumeric()
        number_words += word
    else:
        alphabet_words.append(word)     # x.isalpha()

alphabet_words.sort()
number_words.sort()
sorted_words = "".join(alphabet_words + number_words)

print(sorted_words)