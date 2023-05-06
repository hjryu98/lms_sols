n = int(input())
space = 1
for i in range(1, n + 1):
    print(" " * (n - i), end='')

    if i == 1:
        print("*")
    elif i == n // 2 + 1:
        print("*" * n)
    else:
        print("*", end='')
        print(" " * space, end='')
        print("*")
    if i > 1: space += 2