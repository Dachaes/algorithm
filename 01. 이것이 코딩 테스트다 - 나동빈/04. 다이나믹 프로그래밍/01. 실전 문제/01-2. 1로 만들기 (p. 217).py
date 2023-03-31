# 01. 1로 만들기 (p. 217)

# Input
X = int(input())
make_one = [0] * (X + 1)

for i in range(2, X + 1):
    make_one[i] = make_one[i - 1] + 1
    if i % 2 == 0:
        make_one[i] = min(make_one[i], make_one[i // 2] + 1)
    if i % 3 == 0:
        make_one[i] = min(make_one[i], make_one[i // 3] + 1)
    if i % 5 == 0:
        make_one[i] = min(make_one[i], make_one[i // 5] + 1)

print(make_one[X])