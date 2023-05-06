## template
n, m = map(int, input().split())
cnt = 0
for i in range(n, m + 1):
  print(i, end = ' ')
  cnt += 1
  if cnt == 8:
    cnt = 0
    print()