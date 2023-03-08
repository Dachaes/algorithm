# 6081
n = input()
n = int(n, 16)
for i in range(1, 16):
    print(f"{n:X}*{i:X}={(n * i):X}")
