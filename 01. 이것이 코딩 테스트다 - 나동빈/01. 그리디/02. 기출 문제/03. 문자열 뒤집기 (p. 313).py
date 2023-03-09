# 03. 문자열 뒤집기 (p. 313)

# input
numbers = list(map(int, input()))

# 리스트 내의 연속된 숫자가 몇 묶음 있나?
previous_number = numbers[0]
group_of_num = 1
for number in numbers:
    if previous_number ^ number == 1:
        group_of_num += 1
    previous_number = number

res = group_of_num // 2
print(res)