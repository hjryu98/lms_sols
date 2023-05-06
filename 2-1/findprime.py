## template
n = int(input())
ans = 0
for _ in range(n):
  a = int(input())
  cnt = 0
  for j in range(1, a + 1):
    if a % j == 0: cnt += 1
  if cnt == 2: ans += 1
print(ans)