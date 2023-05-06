## template
n = int(input())
star = 1
space = n - 1
for _ in range(n):
  print(" " * space, end = '')
  print("*" * star)
  star += 2
  space -= 1