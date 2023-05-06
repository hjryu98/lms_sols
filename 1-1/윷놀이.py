## template
for _ in range(3):
  cnt = 0
  arr = list(map(int, input().split()))
  cnt += (arr[0] + arr[1] + arr[2] + arr[3])
  if cnt == 4: print("E")
  elif cnt == 3: print("A")
  elif cnt == 2: print("B")
  elif cnt == 1: print("C")
  else: print("D")