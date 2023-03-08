# 6056
x, y = map(int, input().split())
bool_x = bool(x)
bool_y = bool(y)
print((bool_x and (not bool_y)) or (not(bool_x) and bool_y))
