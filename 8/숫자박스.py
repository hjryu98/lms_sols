## template
def check(x):
  s = 0
  e = n - 1
  while s <= e:
    mid = (s + e) // 2
    if arr[mid] == x: return 1
    if arr[mid] < x: s = mid + 1
    else: e = mid - 1
  return 0

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))

arr.sort()

for i in range(len(query)):
  print(check(query[i]))