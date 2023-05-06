## template
n, m = map(int, input().split())

for i in range(n, m + 1):
  cnt = 0
  for j in range(1, i + 1):
    if i % j == 0: cnt += 1
  if cnt == 2: print(i, end = ' ')