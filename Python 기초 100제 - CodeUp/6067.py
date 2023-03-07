# 6067
def even_or_odd(num):
    if num < 0:
        if num % 2 == 0:
            print("A")
        else:
            print("B")
    else:
        if num % 2 == 0:
            print("C")
        else:
            print("D")

x = int(input())
even_or_odd(x)
