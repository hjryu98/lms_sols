## template
def max(x, y, z):
    if x >= y and x >= z: return x
    if y >= x and y >= z: return y
    if z >= x and z >= y: return z


ans = 0
n = int(input())
for _ in range(n):
    cur = 0
    a, b, c = map(int, input().split())
    if a == b and b == c and a == c:
        cur = 10000 + a * 1000
    else:
        if a == b and b != c:
            cur = 1000 + a * 100
        elif a == c and b != c:
            cur = 1000 + c * 100
        elif b == c and a != c:
            cur = 1000 + b * 100
        else:
            val = max(a, b, c)
            cur = val * 100
    if ans < cur:
        ans = cur

print(ans)