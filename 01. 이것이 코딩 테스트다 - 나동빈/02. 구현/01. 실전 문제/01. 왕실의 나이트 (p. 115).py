# 01. 왕실의 나이트 (p. 115)

# Input
position = input()                  # ex: a1
row = int(position[1])              # ex: 1
column = ord(position[0]) - 96      # ex: a (=1)

routes = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
num_of_possible_paths = 0
for route in routes:
    arrival = (row + route[0], column + route[1])
    if (1 <= arrival[0] <= 8) and (1 <= arrival[1] <= 8):
        num_of_possible_paths += 1

print(num_of_possible_paths)