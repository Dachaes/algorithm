# 35. 못생긴 수 (p. 381)

# Input
n = int(input())
ugly_numbers = [1]

count = 2
while count != (n + 1):
    number = -1
    for ugly_number in ugly_numbers:
        if (ugly_number * 2) not in ugly_numbers:
            if number == -1:
                number = ugly_number * 2
            else:
                number = min(number, ugly_number * 2)
        elif (ugly_number * 3) not in ugly_numbers:
            if number == -1:
                number = ugly_number * 3
            else:
                number = min(number, ugly_number * 3)
        elif (ugly_number * 5) not in ugly_numbers:
            if number == -1:
                number = ugly_number * 5
            else:
                number = min(number, ugly_number * 5)
    ugly_numbers.append(number)
    count += 1

# print(ugly_numbers)
print(ugly_numbers[n - 1])