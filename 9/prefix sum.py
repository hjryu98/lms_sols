## template
n,m = map(int, input().split())
arr = list(map(int, input().split()))
pref = [0] * 100005

for i in range(1, n + 1):
  pref[i] = pref[i - 1] + arr[i - 1]

for _ in range(m):
  a,b = map(int, input().split())
  print(pref[b] - pref[a - 1])
