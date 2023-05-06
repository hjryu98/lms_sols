## template
a = int(input())
b = int(input())
c = int(input())
if a + b + c != 180: print("Error")
else:
  if a == 60 and b == 60 and c == a: print("Equilateral")
  elif (a == b and b != c) or (b == c and a != c) or (a == c and b != c): print("Isosceles")
  else: print("Scalene")