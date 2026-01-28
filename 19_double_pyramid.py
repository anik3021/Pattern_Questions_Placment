n = 3
for i in range(1, n + 1):
    left_spaces = n - i
    stars = 2 * i - 1
    middle_spaces = 2 * (n - i)

    print(" " * left_spaces + "*" * stars +
          " " * middle_spaces +
          "*" * stars)
