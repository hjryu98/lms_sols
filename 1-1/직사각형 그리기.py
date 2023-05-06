## template
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
ansx = 0
ansy = 0

if a == c: ansx = e
if a == e: ansx = c
if c == e: ansx = a
if b == d: ansy = f
if b == f: ansy = d
if d == f: ansy = b
print("{} {}".format(ansx, ansy))