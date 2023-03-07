# 6070
def season(num):
    if num == 12 or num <= 2:
        print("winter")
    elif num <= 5:
        print("spring")
    elif num <= 8:
        print("summer")
    else:
        print("fall")

x = int(input())
season(x)
