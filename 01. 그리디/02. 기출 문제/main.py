# 03. 문자열 뒤집기 (p. 313)

# input
number = list(map(int, input()))

reversed_number = []
for i in range(len(number)):
    reversed_number.append(number[i] ^ 1)

print(reversed_number, end='')

print(sum)
