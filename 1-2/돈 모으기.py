## template
m = int(input())
cur = 1
while m > 0:
  m -= cur
  cur += 1
print(cur - 1)